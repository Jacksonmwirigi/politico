from flask import Flask, Blueprint
from app.api.v1.views.party_views import pt_v1 as v1
from app.api.v1.views.office_views import pt_v2 as v2
from config import app_config

def create_app(config_name):
    """Starting an instance of the flask app"""

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.register_blueprint(v1)
    app.register_blueprint(v2)

    return app
