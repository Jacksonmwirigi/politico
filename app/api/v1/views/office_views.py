from flask import Flask, make_response, request, jsonify
from flask import Blueprint
from app.api.v1.models.offices_model import OfficeModel
from app.validation import*

"""Defining  Office blueprints """
office_bluprint = Blueprint('office_blu', __name__, url_prefix='/api/v1')

@office_bluprint.route('/offices', methods=['POST'])
def create_office():
    """defining office end points for creating a new office """

    key_error = is_office_key_correct(request)
    if key_error:
        return make_response(jsonify({
            "error": 400,
            "msg" : "Invalid keys used"
        }),400)
    data = request.get_json()
    if data :
        office_name = data['office_name']
        office_type = data['office_type']
       
        new_off=OfficeModel().create_office(office_name, office_type)
        return make_response(jsonify({
            "msg": "success" ,
            "status" :201 ,
            "data" :new_off
        }), 201)
 
    else :
        return make_response(jsonify({
            "error" : "No data provided" ,
            "status" :404

    }),404)    

@office_bluprint.route('/offices/<int:office_id>', methods=['GET'])
def get_by_id(office_id):
    """This is the route allows user to retrieve one 
    specific government opffice by specifying the office id"""
    office = OfficeModel().get_office_by_id(office_id)
    if office:
        return make_response(jsonify({
            'msg': 'success',
            'office': office
        }))
    return make_response(jsonify({
        'msg': 'NOt found'
    }))

@office_bluprint.route('/offices', methods=['GET'])
def get_all_offices():
    """This is the route for retrieving all government ofices."""
    offices = OfficeModel().get_all()
    if offices:
        return make_response(jsonify({
            'msg': 'success',
            'offices': offices
        }))
    return make_response(jsonify({
        'msg': 'success',
        'offices': offices
    }))
