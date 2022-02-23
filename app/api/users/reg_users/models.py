import psycopg2
from flask import request, jsonify, make_response, json
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt

from app.database import connection

class Helper():
    
     def check_if_user_exists(self, username):
        """
        Helper function to check if a user exists
        Returns a message if a user already exists
        """
        try:
            connect = connection.dbconnection()
            cursor = connect.cursor(cursor_factory=RealDictCursor)
            cursor.execute("SELECT * FROM users WHERE username = '{}'".format(username))
            connect.commit()
            username = cursor.fetchone()
            cursor.close()
            connect.close()
            if username:
                return True
        except (Exception, psycopg2.DatabaseError) as error:
            return {'error' : '{}'.format(error)}, 401
        
        
class Users(Helper):
    """Handle Users"""
    def reg_user(self, username, email, phone, password, confirm):
        """Method to handle user creation"""
        username = request.json.get('username', None)
        email = request.json.get('email', None)
        phone = request.json.get('phone', None)
        password = request.json.get('password', None)
        confirm = request.json.get('confirm', None)


        present = Helper.check_if_user_exists(self, username)
        if present:
            return jsonify({
                "status": 409,
                "error": "A user with the same username is already registered, please try a new one"
                }), 409

        try:
            hashed_password = generate_password_hash(password)
            add_user = "INSERT INTO \
                        users (username, email, phone, password) \
                        VALUES ('" + username +"', '" + email +"', '" + phone +"', '" + hashed_password +"')"
            connect = connection.dbconnection()
            cursor = connect.cursor()
            cursor.execute(add_user)
            connect.commit()
            get_user = "SELECT username, email, phone, password, user_id \
                        FROM users \
                        WHERE username = '" + username + "'" 
            connect = connection.dbconnection()
            cursor = connect.cursor(cursor_factory=RealDictCursor)
            cursor.execute(get_user)
            row = cursor.fetchone()
            access_token = create_access_token(identity=dict(phone=row["phone"], user_id=row['user_id'], email=row["email"], username=row["username"]))
            response = jsonify({
                        "user":{
                            'phone':row['phone'],
                            'email':row['email'],
                            'username':row['username'],
                            'user_id':row['user_id']
                            },
                        "success":"User Successfully registered", 
                        "access_token":access_token})
            response.status_code = 201
            return (response)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            response = jsonify({'status': 500,
                                'msg':'Problem fetching record from the database'})
            response.status_code = 500
            return response
        
        
    def login_user(self, phone, password):
        """Logs in a user"""

        username = request.json.get('username', None)
        password = request.json.get('password', None)

        # Check for empty inputs
        if username == '' or password == '':
            return{
                "status": 401,
                "error": "Neither of the fields can be left empty during log in"
                }, 401

        try:
            get_user = "SELECT email, username, phone, password,user_id \
                        FROM users \
                        WHERE username = '" + username + "'" 
            connect = connection.dbconnection()
            cursor = connect.cursor(cursor_factory=RealDictCursor)
            cursor.execute(get_user)
            row = cursor.fetchone()
            if row is not None:
                access_token = create_access_token(identity=dict(email=row["email"], name=row["username"], phone=row['phone'], user_id=row["user_id"]))
                valid = check_password_hash(row.get('password'), password)
                if valid:
                    response = jsonify({
                        "user":{
                            'phone':row['phone'],
                            'email':row['email'],
                            'username':row['username']
                            },
                        "success":"User Successfully logged in", 
                        "access_token":access_token})
                    response.status_code = 200
                    return response
            response = jsonify({"status": 401,
                "msg" : "Error logging in, credentials not found"})
            response.status_code = 401
            return response
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            response = jsonify({'status': 500,
                                'msg':'Problem fetching record from the database'})
            response.status_code = 500
            return response
        
    def get_user_by_username(self, username):
        query = "SELECT * from users where username='{}'".format(username)
        connect = connection.dbconnection()
        cursor = connect.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query, (str(username)))
        user = cursor.fetchone()
        if user is not None:
                access_token = create_access_token(identity=dict(username=user["username"]))
                response = jsonify({ 
                        "access_token":access_token,"user":user})
                response.status_code = 200
                return response
        response = jsonify({"status": 401,
            "msg" : "Error logging in, credentials not found"})
        response.status_code = 401
        return response
