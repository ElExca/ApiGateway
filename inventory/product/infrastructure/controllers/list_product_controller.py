from flask import Blueprint, jsonify
from product.application.usecases.list_product import ListProducts

list_product_blueprint = Blueprint('list_product', __name__)

def initialize_list_product_endpoint(repository):
    list_products_usecase = ListProducts(product_repository=repository)

    @list_product_blueprint.route('', methods=['GET'])
    def list_products():
        try:
            products = list_products_usecase.execute()
            return jsonify(products), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404  
