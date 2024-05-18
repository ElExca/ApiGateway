from datetime import datetime

class Order:
    def __init__(self, total, status, order_products=[]):
        self.total = total
        self.date = datetime.now()
        self.status = status
        self.order_products = order_products 
