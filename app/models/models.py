from app import db
from decimal import Decimal

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

class Balance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    account_balance = db.Column(db.Numeric(10, 2), default=Decimal('100000.00'))
    wallet_balance = db.Column(db.Numeric(10, 2), default=Decimal('0.00'))
