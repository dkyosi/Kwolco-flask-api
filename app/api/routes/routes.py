from flask import request, Blueprint, jsonify, Flask, render_template
app = Flask(__name__)

auth_blueprint = Blueprint('auth', __name__)