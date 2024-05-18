from flask import Blueprint, jsonify
from order.application.usecases.list_order import ListOrders

list_order_blueprint = Blueprint('list_order', __name__)

def initialize_list_order_endpoint(order_repository):
    list_orders_usecase = ListOrders(order_repository=order_repository)

    @list_order_blueprint.route('', methods=['GET'])
    def list_orders():
        try:
            orders = list_orders_usecase.execute()
            return jsonify(orders), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404  
