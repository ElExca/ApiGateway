class UpdateOrderStatus:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def execute(self, order_id, new_status):
        return self.order_repository.update_status(order_id, new_status)
