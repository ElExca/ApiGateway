class FindProductByName:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self, name):
        return self.product_repository.find_by_name(name)
