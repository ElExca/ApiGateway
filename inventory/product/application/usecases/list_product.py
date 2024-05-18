class ListProducts:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self):
        products = self.product_repository.find_all()
        if not products:
            raise ValueError("No products available")
        return products
