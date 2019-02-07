from flask import Flask, make_response, request, jsonify
from flask import Blueprint
from app.api.v1.models.gov_offices_model import OfficeModel, offices


pt_v1 = Blueprint('v1', __name__, url_prefix='/api/v1/')


class OfficeView:
    def __init__(self):

    @pt_v1.route('/offices', methods=['POST'])
    def create_office(self):
        data = request.get_json()
        name = data['name']
        candidate_id = data['candidate_id']
        date_created = data['date_created']
        OfficeModel().create_office(name, candidate_id, date_created)

        return make_response(jsonify({
            "msg": "Success"
        }), 201)

        """This is the route allows user to retrieve one specific government opffice by specifying the office id"""

    @pt_v1.route('/offices/<int:office_id>', methods=['GET'])
    def get_by_id(office_id):
        office = OfficeModel().get_party_by_id(office_id)
        if party:
            return make_response(jsonify({
                'msg': 'success',
                'office': office
            }))
        return make_response(jsonify({
            'msg': 'NOt found'
        }))

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
