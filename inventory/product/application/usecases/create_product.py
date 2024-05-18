from product.domain.entities.product import Product
from product.domain.validations.product_validations import validate_product

class CreateProduct:
    def __init__(self, product_repository):
        self.product_repository = product_repository

    def execute(self, name, price, stock):
        product = Product(name, price, stock)
        validate_product(product)
        self.product_repository.save(product)
