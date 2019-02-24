from app.api.v2.models.office_model import Offices
from app.api.v2.models.base_model import BaseModel
from flask import Flask,Blueprint ,make_response, jsonify, request
from flask.views import MethodView
from app.validation import*

office_bluprint=Blueprint('offices',__name__, url_prefix="/api/v2")

@office_bluprint.route('/offices',methods=['POST'])
def post_office():
    """Adding new office record into the database"""
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

@office_bluprint.route('/offices', methods=['GET'])
def view_all_offices():
    """retrieves all the registered offices."""
    offices= Offices.get_all_offices()
    if offices:
        return make_response(jsonify({
            'status': 200,
            'message': 'Successful',
            'data': offices
            
        }),200)
    return make_response(jsonify({
        'status': 404,
        'message': 'no office to display'
    }),404) 

@office_bluprint.route('/offices/<int:office_id>',methods=['GET'])
def view_one_office(office_id):
    """retrieves one specific government office by the office_id"""
    if BaseModel().check_if_exists('offices','office_id',office_id):
        office=Offices.get_one_office(office_id)
        return make_response(jsonify({
            "status":200,
            "msg" :"success",
            "data": office
        }))
    return  make_response(jsonify({
        "error":404,
        "msg":"No such office found"
    }))