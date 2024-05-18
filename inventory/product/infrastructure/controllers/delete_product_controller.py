from flask import Blueprint, request, jsonify
from product.application.usecases.delete_product import DeleteProduct

delete_product_blueprint = Blueprint('delete_product', __name__)

def initialize_delete_product_endpoint(repository):
    delete_product_usecase = DeleteProduct(product_repository=repository)

    @delete_product_blueprint.route('/<product_id>', methods=['DELETE'])
    def delete_product(product_id):
        try:
            delete_product_usecase.execute(product_id)
            return jsonify({"message": "Product eliminado exitosamente"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404 
