from flask import Blueprint, request, jsonify
from order.application.usecases.create_order import CreateOrder
from order.infrastructure.repositories.order_repository import MongoDBOrderRepository

order_blueprint = Blueprint('order', __name__)

def initialize_order_endpoint(order_repository):
    create_order_usecase = CreateOrder(order_repository)

    @order_blueprint.route('', methods=['POST'])
    def create_order():
        data = request.get_json()
        try:
            create_order_usecase.execute(data['product_names'], data['quantities'])
            return jsonify({"message": "Orden creada exitosamente"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400
