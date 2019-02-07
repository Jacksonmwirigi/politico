from flask import Flask, jsonify, request, make_response, Blueprint, Response
from app.api.v1.models.parties_model import Party


"""The below file reisters blueprints for the api"""
pt_v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

"""this class represents party views"""

"""this class represnts party views"""

"""This end point allows uadmin to create a new political party"""
@pt_v1.route('/parties', methods=['POST'])
def create__a_party():
    data = request.get_json()
    name = data['name']
    hqAddress = data['hqAddress']
    logoUrl = data['logoUrl']
    party = Party().create_party(name, hqAddress, logoUrl)
    return make_response(jsonify({
        "data": party,
        "status": 201,
        "msg": "created Successfully"

    }), 201)


"""This is the route for retrieving all political parties."""


@pt_v1.route('/parties', methods=['GET'])
def get_all_parties():
    parties = Party().get_all()
    if parties:
        return make_response(jsonify({
            'msg': 'success',
            'parties': parties
        }))


"""This is the route allows user to retrieve one political party with specific party id"""


@pt_v1.route('/parties/<int:party_id>', methods=['GET'])
def get_by_id(party_id):
    party = Party().get_party_by_id(party_id)
    if party:
        return make_response(jsonify({
            'message': 'success',
            'Status': 200,
            'parties': party
        }), 200)
    return make_response(jsonify({
        'error': 404,
        'message': 'NOt found'
    }), 404)


"""This end point allow admin to edit a party by creating a PATCH request on postman"""
@pt_v1.route('/parties/<int:party_id>/name', methods=['PUT'])
def edit_party_name(party_id):
    data = request.get_json
    party = Party().edit_party(party_id, data)
    return make_response(jsonify({
        'status': 'OK',
        'message': 'update successful',
        'parties': party
    }), 200)


@pt_v1.route('/editparties<party_id>', methods=['DELETE'])
def delete_a_party(self, party_id):
    Party().delete_party(party_id)
    return make_response(jsonify({
        'status': 'OK',
        'message': 'successfully deleted'
    }), 200)
