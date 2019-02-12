from flask import Flask, Blueprint
from app.api.v1.views.party_views import party_bluprint  
from app.api.v1.views.office_views import office_bluprint 
# from app.api.v1.views.office_views import pt_v2 as v2
from config import app_config

def create_app(config_name):
    """Starting an instance of the flask app"""
    app = Flask(__name__)       
    app.config.from_object(app_config[config_name])
    app.register_blueprint(party_bluprint)
    app.register_blueprint(office_bluprint)

    return app
