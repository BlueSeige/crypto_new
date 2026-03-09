import os

class Config:
    SECRET_KEY = "supersecretkey"
    _db_url = os.getenv("DATABASE_URL", "").strip()
    if not _db_url:
        raise RuntimeError("DATABASE_URL is required. SQLite fallback has been disabled.")
    if _db_url.startswith("postgres://"):
        _db_url = _db_url.replace("postgres://", "postgresql://", 1)
    SQLALCHEMY_DATABASE_URI = _db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #custodial deposit addresses (set them here)
    #Users will see these as their "deposit address" in the UI.
    DEPOSIT_ADDRESSES = {
        "USDT": {
            "TRC20": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "ERC20": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "BEP20": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "POLYGON": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "ARBITRUM": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "OPTIMISM": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "SOL": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
        },
        "USDC": {
            "ERC20": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "BEP20": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "POLYGON": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "ARBITRUM": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "OPTIMISM": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "SOL": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
        },
        "CAD": {
            "INTERAC": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "SWIFT": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "WIRE": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7"
        },
        "BTC": {
            "BTC": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7"
        },
        "ETH": {
            "ETH": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "ARBITRUM": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
            "OPTIMISM": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7",
        },
        "BNB": {
            "BEP20": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7"
        },
        "SOL": {
            "SOL": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7"
        },
        "XRP": {
            "XRP": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7"
        },
        "TRX": {
            "TRC20": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7"
        },
        "LTC": {
            "LTC": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7"
        },
        "DOGE": {
            "DOGE": "bc1q54zz8x0dg494j76z6rnvy72rqrm7al06q2rrf7"
        },
    }




