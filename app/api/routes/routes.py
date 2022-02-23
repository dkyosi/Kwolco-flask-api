from flask import request, Blueprint, jsonify, Flask, render_template
app = Flask(__name__)

auth_blueprint = Blueprint('auth', __name__)

"""Importing endpoints"""
from app.api.users.reg_users.views import NewUsers,LoginUser,GetUserByUsername

"""Define the api endpoints"""
registration_of_users = NewUsers.as_view('register_api')
reg_user_login = LoginUser.as_view('login_api')
get_user_view_username = GetUserByUsername.as_view('user_by_username')


"""User registration"""
auth_blueprint.add_url_rule(
    '/api/v1/signup', 
    view_func=registration_of_users,
    methods=['POST'])

"""User login"""
auth_blueprint.add_url_rule(
    '/api/v1/login',
    view_func=reg_user_login,
    methods=['POST'])

"""Get User Profile"""
auth_blueprint.add_url_rule(
    '/api/v1/users/<username>',
    view_func=get_user_view_username,
    methods=['GET'])