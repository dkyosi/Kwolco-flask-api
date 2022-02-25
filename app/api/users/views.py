"""Views for the Users Resource"""

from flask_restful import Resource, reqparse
from flask import request, Blueprint, jsonify, Flask
app = Flask(__name__)
from app.api.users.models import Users
from app.api.validators.validator import validate_data_signup

auth_blueprint = Blueprint('auth', __name__)

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('username', help="You must supply your username", required='True')
parser.add_argument('email', help="You must supply your email", required='False')
parser.add_argument('phone', help="You must supply your no", required='True')
parser.add_argument('password', help="You must supply a password", required='True')
parser.add_argument('confirm', help="You must supply a confirmation for your password", required='True')

class NewUsers(Resource):
    """Class to handle adding users"""
    def post(self):
        """Route to handle creating users"""
        args = parser.parse_args()
        response = validate_data_signup(args)
        if response == "valid":
            return Users().reg_user(
                args['username'],
                args['email'],
                args['phone'],
                args['password'],
                args['confirm'])
        return jsonify(response)
    
class LoginUser(Resource):
    """Class to handle user login"""
    def post(self):
        return Users().login_user(
            request.json['username'],
            request.json['password'])
        
class GetUserByUsername(Resource):
    """Get user by username"""
    def get(self,username):
        """Route to fetch a specific user"""
        return Users().get_user_by_username(str(username))