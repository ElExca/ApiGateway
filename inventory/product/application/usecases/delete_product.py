class DeleteProduct:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self, product_id):
        self.product_repository.delete_by_id(product_id)
