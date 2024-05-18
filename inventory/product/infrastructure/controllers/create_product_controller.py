from flask import Blueprint, request, jsonify
from product.application.usecases.create_product import CreateProduct

product_blueprint = Blueprint('product', __name__)

def initialize_product_endpoint(repository):
    create_product_usecase = CreateProduct(product_repository=repository)

    @product_blueprint.route('', methods=['POST'])
    def create_product():
        data = request.get_json()
        try:
            create_product_usecase.execute(data['name'], data['price'], data['stock'])
            return jsonify({"message": "Producto creado exitosamente"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 409 
        except Exception as e:
            return jsonify({"error": str(e)}), 400