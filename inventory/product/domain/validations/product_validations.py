def validate_product(product):
    if not product.name:
        raise ValueError("Product name cannot be empty")
    if type(product.name) is not str:
        raise ValueError("Product name must be a string")
    if product.price <= 0:
        raise ValueError("Product price must be positive")
    if type(product.price) not in [int, float]:
        raise ValueError("Product price must be a number")
    if product.stock < 0:
        raise ValueError("Product stock cannot be negative")
    if type(product.stock) is not int:
        raise ValueError("Product stock must be an integer")
