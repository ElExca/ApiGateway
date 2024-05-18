import requests
from order.domain.entities.order import Order
from order.domain.entities.order_product import OrderProduct
from order.domain.validations.order_validations import validate_order

class CreateOrder:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def execute(self, product_names, quantities):
        inventory_url = "http://localhost:8080/api/products/search"  # URL actualizada

        order_products = []
        total = 0
        for name, qty in zip(product_names, quantities):
            response = requests.get(inventory_url, params={"name": name})  # Asegúrate de que los parámetros son correctos
            if response.status_code == 200 and response.json():
                product_data = response.json()[0]  # Asumiendo que la respuesta es una lista
                order_product = OrderProduct(product_data["_id"], product_data["price"], qty)
                order_products.append(order_product)
                total += product_data["price"] * qty
            else:
                raise Exception(f"Producto {name} no encontrado en el inventario")

        order = Order(total=total, status="Creado", order_products=order_products)
        validate_order(order)
        self.order_repository.save(order)
