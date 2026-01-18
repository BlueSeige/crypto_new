from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname  = db.Column(db.String(80), nullable=False)
    email     = db.Column(db.String(120), unique=True, nullable=False)

    password  = db.Column(db.String(200), nullable=False)


class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)

    coin = db.Column(db.String(12), nullable=False)         # e.g. "USDT", "BTC"
    amount = db.Column(db.Float, nullable=False, default=0) # user's balance
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint("user_id", "coin", name="uq_user_coin"),
    )




class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    type = db.Column(db.String(50), nullable=False)      # DEPOSIT / ADMIN_SET / ADMIN_ADJUST ...
    coin = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    status = db.Column(db.String(20), nullable=False, default="CONFIRMED")  # PENDING/CONFIRMED
    note = db.Column(db.String(255), nullable=True)
    network = db.Column(db.String(30), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
