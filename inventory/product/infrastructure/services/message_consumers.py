import pika
import json
from inventory.product.infrastructure.repositories.product_repository import MongoDBProductRepository

def update_product_stock(order_details):
    repository = MongoDBProductRepository(connection_string='mongodb://localhost:27017/', database_name='inventory')
    for product in order_details['order_products']:
        product_id = product['product_id']
        quantity = product['quantity']
        repository.decrease_stock(product_id, quantity)

def callback(ch, method, properties, body):
    order_details = json.loads(body)
    update_product_stock(order_details)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='stock_updates')

channel.basic_consume(
    queue='stock_updates',
    on_message_callback=callback,
    auto_ack=True
)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
