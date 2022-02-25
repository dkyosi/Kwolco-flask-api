from flask_restful import Resource, reqparse
from flask import request
from app.api.products.models import Products

class NewProduct(Resource):
     def post(self):
        return Products().create_new_product(
            request.json['product_name'],
            request.json['tones'],
            request.json['country_id'],
            request.json['price_per_kg'])
        
        
class GetProductById(Resource):
    """Get product by id"""
    def get(self,id):
        """Route to fetch a specific product"""
        return Products().get_product_by_id(str(id))
    
class UpdateProduct(Resource):
    def put(self,id):
        return Products().update_product(
            str(id),
            request.json['product_name'],
            request.json['tones'], 
            request.json['country_id'], 
            request.json['price_per_kg'])
        
class DeleteProduct(Resource):
    def delete(self,id):
        return Products().delete_product(str(id))
    
class GetAllProducts(Resource):
    def get(self):
        return Products().get_all_products()