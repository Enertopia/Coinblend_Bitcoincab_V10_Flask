from app.models.models import Balance, db
from flask import current_app as app
from decimal import Decimal

def convert_to_bitcoin(user_id, amount_fiat, conversion_percentage):
    balance = Balance.query.filter_by(user_id=user_id).first()
    conversion_rate = Decimal(app.config['CONVERSION_RATE'])
    amount_to_convert = Decimal(amount_fiat) * Decimal(conversion_percentage)
    amount_to_wallet = amount_to_convert * conversion_rate

    balance.account_balance -= amount_to_convert
    balance.wallet_balance += amount_to_wallet
    db.session.commit()

    return {'amount_to_wallet': str(amount_to_wallet)}
