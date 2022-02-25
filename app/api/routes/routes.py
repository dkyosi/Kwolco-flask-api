from flask import request, Blueprint, jsonify, Flask, render_template
app = Flask(__name__)

auth_blueprint = Blueprint('auth', __name__)

"""Importing endpoints"""
from app.api.users.views import NewUsers,LoginUser,GetUserByUsername
from app.api.countries.views import GetCountries
from app.api.products.views import NewProduct,GetProductById,UpdateProduct,DeleteProduct,GetAllProducts

"""Define the api endpoints"""
registration_of_users = NewUsers.as_view('register_api')
reg_user_login = LoginUser.as_view('login_api')
get_user_view_username = GetUserByUsername.as_view('user_by_username')

get_all_countries = GetCountries.as_view('all_countries')


create_new_product = NewProduct.as_view('new_product')
get_product_by_id = GetProductById.as_view('get_product')
update_product_details = UpdateProduct.as_view('update_product')
delete_product = DeleteProduct.as_view('delete_product')
get_all_products = GetAllProducts.as_view('get_all_products')

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

"""Get all countries"""
auth_blueprint.add_url_rule(
    '/api/v1/countries',
    view_func=get_all_countries,
    methods=['GET']
)


"""Create new product"""
auth_blueprint.add_url_rule(
    '/api/v1/products/create', 
    view_func=create_new_product,
    methods=['POST'])

"""Get Product By Id"""
auth_blueprint.add_url_rule(
    '/api/v1/products/<id>',
    view_func=get_product_by_id,
    methods=['GET'])

"""Update Product"""
auth_blueprint.add_url_rule(
    '/api/v1/products/<id>',
    view_func=update_product_details,
    methods=['PUT'])

"""Update Product"""
auth_blueprint.add_url_rule(
    '/api/v1/products/<id>',
    view_func=delete_product,
    methods=['DELETE'])

"""Get All Products"""
auth_blueprint.add_url_rule(
    '/api/v1/products',
    view_func=get_all_products,
    methods=['GET'])