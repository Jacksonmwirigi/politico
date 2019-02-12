from flask import Flask, jsonify, request, make_response, Blueprint, Response
from app.api.v1.models.parties_model import Party

"""The below file reisters blueprints for the api"""
pt_v1 = Blueprint('v1', __name__, url_prefix='/api/v1')


@pt_v1.route('/parties', methods=['POST'])
def create__a_party():
    """This end point allows Admin to create a new political party"""
    data = request.get_json()
    name = data['name']
    hqAddress = data['hqAddress']
    logoUrl = data['logoUrl']
    Party().create_party(name, hqAddress, logoUrl)
    return make_response(jsonify({
        "data": data,
        "status": 201,
        "msg": "created Successfully"

    }), 201)



@pt_v1.route('/parties', methods=['GET'])
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
        'message': 'NOt found'
    }), 404)



@pt_v1.route('/parties/<int:party_id>', methods=['GET'])
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
        'message': 'NOt found'
    }), 404)


@pt_v1.route('/parties/<int:party_id>/name', methods=['PUT'])
def edit_party_name(party_id):
    """ End point for edit party by sending a PUT request on postman"""
    data = request.get_json
    party = Party().edit_party(party_id, data)
    return make_response(jsonify({
        'status': 'OK',
        'message': 'update successful',
        'parties': party
    }), 200)



@pt_v1.route('/parties/<party_id>', methods=['DELETE'])
def delete_a_party(self, party_id):
    """This method checks for an existing party then deletes it """
    if Party().delete_party(party_id):
    # party = Party().if_party_exists(party_id)

        return make_response(jsonify({
                'status': 200,
                'message': "Deleted successfully"
            }), 200)
    return make_response(jsonify({
            'status': 404,
            'message': 'party does not exist'
        }), 404)

    # if party:
    #     respo = Party().delete_party(party)

    #     return make_response(jsonify({
    #         'status': 200,
    #         'message': "Deleted successfully"
    #     }), 200)
    # else:
    #     return make_response(jsonify({
    #         'status': 404,
    #         'message': 'party does not exist'
    #     }), 404)
