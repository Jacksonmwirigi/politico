from flask import Flask
from flask import Blueprint
from app.api.v1.views.party_views import Parties
from app.api.v1.views.party_views import pt_v1 as v1

"""Creating an instance of the flask app"""
def create_app():
    app = Flask(__name__)

    app.register_blueprint(v1)

    return app
