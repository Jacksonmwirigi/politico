from flask import Flask, jsonify, request, make_response, Blueprint, Response
from app.api.v1.models.parties_model import Party


"""The below file reisters blueprints for the api"""
pt_v1 = Blueprint('v1', __name__, url_prefix='/api/v1/')

"""this class represents party views"""


class Parties:
    """this class represnts party views"""

    @pt_v1.route('/parties', methods=['POST'])
    def create__a_party():
        data = request.get_json()
        name = data['name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']
        Party().create_party(name, hqAddress, logoUrl)
        #new_party = Party().create_party(name, hqAddress, logoUrl)
        return make_response(jsonify({
            "msg": "Success"
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
        return make_response(jsonify({
            'msg': 'success',
            'parties': parties
        }))

    @pt_v1.route('/parties/<int:party_id>', methods=['GET'])
    def get_by_id( party_id):
        party = Party().get_party_by_id(party_id)
        if party:
            return make_response(jsonify({
                'msg': 'success',
                'parties': party
            }))
        return make_response(jsonify({
            'msg': 'NOt found'
        }))    


