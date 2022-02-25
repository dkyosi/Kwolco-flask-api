import psycopg2
from flask import request, jsonify, make_response, json
from psycopg2.extras import RealDictCursor
from app.database import connection

class Countries():
    """Handle countries"""
    def get_countries(self):
        try:
            get_country = """SELECT * FROM countries"""
            connect = connection.dbconnection()
            cursor = connect.cursor(cursor_factory=RealDictCursor)
            cursor.execute(get_country)
            countries = cursor.fetchall()
            response = jsonify({
                "status":200,
                "countries":countries
            })
            response.status_code = 200
            return (response)
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            response = jsonify({'status': 500,
                                'msg':'Problem fetching countries from the database'})
            response.status_code = 500
            return response