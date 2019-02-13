from flask import Flask, jsonify, request, make_response, Blueprint, Response
from app.api.v1.models.parties_model import Party, PARTY_LIST
from app.validation import*

"""The below file reisters blueprints for the api"""
party_bluprint = Blueprint('party_blu', __name__, url_prefix='/api/v1')


@party_bluprint.route('/parties', methods=['POST'])
def create__a_party():
    """This end point allows Admin to create a new political party"""
    invalid_keys = is_party_key_correct(request)
    if invalid_keys:
        return make_response(jsonify({
            "error": 400,
            "msg": "Invalid keys used"
        }))
        
    data = request.get_json()
    if data:
        name = data['name'],
        hqAddress = data['hqAddress'],
        logoUrl = data['logoUrl']

        if valid_url_extension(logoUrl):
            Party().create_party(name, hqAddress, logoUrl)
            return make_response(jsonify({
                "data": data,
                "status": 201,
                "msg": "created Successfully"
            }), 201)
        else:
            return "invalid image url"
    else:
        return make_response(jsonify({
            "error": "No data provided! Party not created",
            "status": 400,
        }), 400)


@party_bluprint.route('/parties', methods=['GET'])
def get_all_parties():
    """This is the route for retrieving all political parties."""
    parties = Party().get_all()
    if parties:
        return make_response(jsonify({
            'msg': 'success',
            'status': 200,
            'parties': parties
        }), 200)
    return make_response(jsonify({
        'error': 404,
        'message': 'Nothing to display'
    }), 404)


@party_bluprint.route('/parties/<int:party_id>', methods=['GET'])
def get_by_id(party_id):
    """Retrieve one political party with specific party id"""
    party = Party().get_party_by_id(party_id)
    if party:
        return make_response(jsonify({
            'message': 'success',
            'Status': 200,
            'parties': party
        }), 200)
    return make_response(jsonify({
        'error': 404,
        'message': 'Nothing to display'
    }), 404)


@party_bluprint.route('/parties/<int:party_id>', methods=['PATCH'])
def edit_party_name(party_id):
    """ End point for edit party by sending a PATCH request on postman"""
    data = request.get_json()
    party = Party().edit_party(party_id, data)
    if party:
        return make_response(jsonify({
            'status': 200,
            'message': 'update successful',
            'parties': party
        }), 201)
    return make_response(jsonify({
        'status': 404,
        'message': 'Not found'
    }), 404)


@party_bluprint.route('/parties/<int:party_id>', methods=['DELETE'])
def delete_a_party(party_id):
    """This method checks for an existing party then deletes it """
    for party in PARTY_LIST:
        if party['party_id'] == party_id:
            Party().delete_party(party_id)
            return make_response(jsonify({
                'status': 200,
                'message': "Deleted successfully"
            }), 200)
    else:
        return make_response(jsonify({
            'status': 404,
            'message': 'party does not exist'
        }), 404)
