from pymongo import MongoClient
from bson import ObjectId
from order.domain.entities.order import Order

class MongoDBOrderRepository:
    def __init__(self, connection_string, database_name):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.order_collection = self.db['order']

    def save(self, order: Order):
        order_data = {
            "total": order.total,
            "date": order.date,
            "status": order.status,
            "order_products": [{"product_id": p.product_id, "price": p.price, "quantity": p.quantity} for p in order.order_products]
        }
        self.order_collection.insert_one(order_data)

    def find_all(self):
        orders = list(self.order_collection.find({}))
        if not orders:
            raise ValueError("No existen ordenes")
        # Convertir ObjectId a string
        return [{
            "_id": str(order["_id"]),
            "total": order["total"],
            "date": order["date"],
            "status": order["status"],
            "order_products": [{"product_id": str(p["product_id"]), "price": p["price"], "quantity": p["quantity"]} for p in order["order_products"]]
        } for order in orders]
    
    def update_status(self, order_id, new_status):
        result = self.order_collection.update_one(
            {"_id": ObjectId(order_id)},
            {"$set": {"status": new_status}}
        )
        if result.matched_count == 0:
            raise ValueError("Orden no encontrada")
        if result.modified_count == 0:
            raise ValueError("El estatus no fue actualizado")
        return True