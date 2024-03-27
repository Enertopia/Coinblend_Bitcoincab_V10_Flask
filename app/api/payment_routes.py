from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ..services.conversion_service import convert_to_bitcoin

payment_bp = Blueprint('payment_bp', __name__)

@payment_bp.route('/convert', methods=['POST'])
@jwt_required()
def convert():
    user_id = get_jwt_identity()
    data = request.get_json()
    result = convert_to_bitcoin(user_id, data['amount_fiat'], data.get('conversion_percentage', 0.05))
    return jsonify(result)
