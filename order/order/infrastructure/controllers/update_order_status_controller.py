from flask import Blueprint, request, jsonify
from order.application.usecases.update_order_status import UpdateOrderStatus

update_order_status_blueprint = Blueprint('update_order_status', __name__)

def initialize_update_order_status_endpoint(order_repository):
    update_order_status_usecase = UpdateOrderStatus(order_repository=order_repository)

    @update_order_status_blueprint.route('/update_status/<order_id>', methods=['PUT'])
    def update_order_status(order_id):
        new_status = request.json.get('status')
        if not new_status:
            return jsonify({"error": "Estatus es requerido"}), 400
        try:
            update_order_status_usecase.execute(order_id, new_status)
            return jsonify({"message": "Estatus actualizado exitosamente"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
