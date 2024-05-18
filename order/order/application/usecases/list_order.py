class ListOrders:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def execute(self):
        return self.order_repository.find_all()
