import argparse
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import db, User, Asset, Transaction


def normalize_postgres_url(url: str) -> str:
    if url.startswith("postgres://"):
        return url.replace("postgres://", "postgresql://", 1)
    return url


def parse_args():
    parser = argparse.ArgumentParser(
        description="Migrate data from SQLite to PostgreSQL for this app."
    )
    parser.add_argument(
        "--sqlite-uri",
        default=os.getenv("SQLITE_URI", "sqlite:////data/database.db"),
        help="Source SQLite URI (default: sqlite:////data/database.db or SQLITE_URI env var).",
    )
    parser.add_argument(
        "--postgres-uri",
        default=os.getenv("DATABASE_URL", ""),
        help="Target PostgreSQL URI (default: DATABASE_URL env var).",
    )
    parser.add_argument(
        "--skip-truncate",
        action="store_true",
        help="Do not clear existing target tables before inserting rows.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    postgres_uri = normalize_postgres_url((args.postgres_uri or "").strip())

    if not postgres_uri:
        raise SystemExit("Missing --postgres-uri (or DATABASE_URL env var).")

    src_engine = create_engine(args.sqlite_uri)
    dst_engine = create_engine(postgres_uri)

    SrcSession = sessionmaker(bind=src_engine)
    DstSession = sessionmaker(bind=dst_engine)

    # Ensure tables exist in Postgres before copying rows.
    db.metadata.create_all(bind=dst_engine)

    src = SrcSession()
    dst = DstSession()
    try:
        if not args.skip_truncate:
            for table in reversed(db.metadata.sorted_tables):
                dst.execute(table.delete())
            dst.commit()

        for model in (User, Asset, Transaction):
            rows = src.query(model).all()
            mappings = []
            for row in rows:
                mappings.append(
                    {col.name: getattr(row, col.name) for col in model.__table__.columns}
                )
            if mappings:
                dst.bulk_insert_mappings(model, mappings)
                dst.commit()
            print(f"{model.__name__}: migrated {len(mappings)} row(s)")

        print("Migration complete.")
    finally:
        src.close()
        dst.close()


if __name__ == "__main__":
    main()
