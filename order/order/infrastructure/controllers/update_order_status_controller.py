import pika
import json
from flask import Blueprint, request, jsonify
from order.application.usecases.update_order_status import UpdateOrderStatus
from order.infrastructure.repositories.order_repository import OrderRepository  # Asegúrate de importar correctamente tu repositorio

update_order_status_blueprint = Blueprint('update_order_status', __name__)

def initialize_update_order_status_endpoint(order_repository):
    update_order_status_usecase = UpdateOrderStatus(order_repository=order_repository)

    @update_order_status_blueprint.route('/update_status/<order_id>', methods=['PUT'])
    def update_order_status(order_id):
        new_status = request.json.get('status')
        if not new_status:
            return jsonify({"error": "Estatus es requerido"}), 400
        try:
            updated = update_order_status_usecase.execute(order_id, new_status)
            if new_status == 'Enviado':
                order_details = order_repository.get_order_by_id(order_id)  # Utiliza el método del repositorio
                send_stock_update_message(order_details)
            return jsonify({"message": "Estatus actualizado exitosamente"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

def send_stock_update_message(order_details):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='stock_updates')

    channel.basic_publish(
        exchange='',
        routing_key='stock_updates',
        body=json.dumps(order_details)
    )
    connection.close()
