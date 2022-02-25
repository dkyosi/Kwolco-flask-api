import psycopg2
from flask import request, jsonify, make_response, json
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from psycopg2.extras import RealDictCursor
from app.database import connection

class Products():
    
    @jwt_required
    def create_new_product(self,product_name,tones,country_id,price_per_kg):
        
        product_name = request.json.get('product_name', None)
        tones = request.json.get('tones', None)
        country_id = request.json.get('country_id', None)
        price_per_kg = request.json.get('price_per_kg', None)
        
        try:
             add_product = "INSERT INTO \
                        products (country_id, product_name, tones, price_per_kg) \
                        VALUES ('" + country_id +"', '" + product_name +"', '" + tones +"', '" + price_per_kg +"')"
             connect = connection.dbconnection()
             cursor = connect.cursor()
             cursor.execute(add_product)
             connect.commit()
            
             response = jsonify({
                 'status':201,
                 'message':'Product created successfully'
             })
             response.status_code = 201
             return (response)
             
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            response = jsonify({'status': 500,
                                'msg':'Problem saving product to the database'})
            response.status_code = 500
            return response
        
    @jwt_required    
    def get_product_by_id(self, id):
        query = "SELECT * from products where product_id='{}'".format(id)
        connect = connection.dbconnection()
        cursor = connect.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query, (str(id)))
        product = cursor.fetchone()
        if product is not None:
                response = jsonify({ 
                       "product":product})
                response.status_code = 200
                return response
        response = jsonify({"status": 404,
            "message" : "Product Not Found 404"})
        response.status_code = 404
        return response
    
    @jwt_required
    def update_product(self,id,product_name,tones,country_id,price_per_kg):
         connect = connection.dbconnection()
         cursor = connect.cursor(cursor_factory=RealDictCursor)
         try:
            query = "UPDATE products SET product_name=%s,tones=%s,country_id=%s,price_per_kg=%s WHERE product_id=%s"
            cursor.execute(query, (product_name, tones, country_id,price_per_kg, id ))
            connect.commit()
            return jsonify({'status': 200,
                            'message': 'Product updated succesfully'})
         except Exception as e:
            print(e)
         connect.close()
         return jsonify({'message':'Cannot update product','status':500})
     
    @jwt_required 
    def delete_product(self,id):
         try:
             query = 'DELETE from products where product_id=%s'
             connect = connection.dbconnection()
             cursor = connect.cursor()
             cursor.execute(query,(id))
             connect.commit()
             connect.close()
             return jsonify({'status': 204,
                            'message': 'Product deleted succesfully'})
             
         except Exception as e:
            print(e)
         return jsonify({'message':'Cannot delete product','status':500})
     
    @jwt_required
    def get_all_products(self):
        try:
            get_country = """SELECT * FROM products"""
            connect = connection.dbconnection()
            cursor = connect.cursor(cursor_factory=RealDictCursor)
            cursor.execute(get_country)
            products = cursor.fetchall()
            response = jsonify({
                "status":200,
                "products":products
            })
            response.status_code = 200
            return (response)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            response = jsonify({'status': 500,
                                'msg':'Problem fetching products from the database'})
            response.status_code = 500
            return response