from app.api.v2.models.office_model import Offices
from app.api.v2.models.base_model import BaseModel
from flask import Flask,Blueprint ,make_response, jsonify, request
from flask.views import MethodView
from app.validation import*

office_bluprint=Blueprint('offices',__name__, url_prefix="/api/v2")

@office_bluprint.route('/offices',methods=['POST'])
def post_office():
    data =request.get_json()
    if data:
        office_name= data['office_name']
        office_type=data['office_type']

    nw_office= Offices(office_name,office_type).register_office()
    return make_response(jsonify({
        "status":201,
        "msg":"registered successfully ",
        "data":nw_office
    }))  

