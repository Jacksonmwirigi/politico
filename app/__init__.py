from flask import Flask, Blueprint
from app.api.v1.views.party_views import Parties
from app.api.v1.views.party_views import pt_v1 as v1
from app.api.v1.views.office_views import pt_v2 as v2

"""Creating an instance of the flask app"""
def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1)
    app.register_blueprint(v2)
   

    return app