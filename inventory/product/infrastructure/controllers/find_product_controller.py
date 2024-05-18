from flask import Blueprint, request, jsonify
from product.application.usecases.find_product import FindProductByName

find_product_by_name_blueprint = Blueprint('find_product_by_name', __name__)

def initialize_find_product_by_name_endpoint(repository):
    find_product_by_name_usecase = FindProductByName(product_repository=repository)

    @find_product_by_name_blueprint.route('/search', methods=['GET'])
    def find_product_by_name():
        name = request.args.get('name', '')
        try:
            products = find_product_by_name_usecase.execute(name)
            return jsonify(products), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404  # Not Found
