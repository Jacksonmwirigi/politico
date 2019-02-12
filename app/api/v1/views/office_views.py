from flask import Flask, make_response, request, jsonify
from flask import Blueprint
from app.api.v1.models.offices_model import OfficeModel

"""Defining  Office blueprints """
office_bluprint = Blueprint('office_blu', __name__, url_prefix='/api/v1')

@office_bluprint.route('/offices', methods=['POST'])
def create_office():
    """defining office end points for creating a new office """
    data = request.get_json()
    name = data['name']
    candidate_id = data['candidate_id']
    date_created = data['date_created']
    OfficeModel().create_office(name, candidate_id, date_created)
    return make_response(jsonify({
        "msg": "success"
    }), 201)

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



