from flask import Flask, Blueprint
from app.api.v1.views.party_views import party_bluprint
from app.api.v1.views.office_views import office_bluprint
from app.api.v2.views.auth.user_view import register_bluprint, login_bluprint
from app.api.v2.views.parties_view import party_bluprint
from app.api.v2.views.office_views import office_bluprint

from app.validation import*
# from app.api.v1.views.office_views import pt_v2 as v2
from config import app_config


def create_app(config_name):
    """Starting an instance of the flask app"""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.register_blueprint(party_bluprint)
    app.register_blueprint(office_bluprint)
    app.register_blueprint(register_bluprint)
    app.register_blueprint(login_bluprint)
    app.register_blueprint(office_bluprint)
    app.register_blueprint(party_bluprint)
    app.register_error_handler(400, bad_request)
    app.register_error_handler(500, internal_server_error)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, method_not_allowed)
    # app.register_error_handler('Type error', type_error)
    return app
