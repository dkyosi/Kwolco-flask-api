import os
from flask import Flask, redirect, jsonify,render_template
from flask_restful import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import datetime, timedelta

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False
    CORS(app)
    
    
    def configure_blueprints(app):
        """ Configure blueprints . """
        from app.api.routes.routes import auth_blueprint

        app_blueprints = [ auth_blueprint ]

        for bp in app_blueprints:
            CORS(bp)
            app.register_blueprint(bp)

    """register the blueprints"""
    configure_blueprints(app)
    
    
    #initializedb()
    app.config['JWT_SECRET_KEY'] = 'SECRET'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=100) 
    jwt = JWTManager(app)
    app.secret_key = "secret key"
    
    return app