from flask import Flask, jsonify, request, make_response, Blueprint
from app.api.v1.models.parties_model import Party

pt_v1 = Blueprint('v1', __name__, url_prefix='/api/v1/')


class Parties:
    """this class represnts party views"""

    @pt_v1.route('/parties', methods=['POST'])
    def create_party():
        
        data = request.get_json()
        name = data['name']
        hqAddress = data['hqAddress']
        logoUrl = data['logoUrl']
        new_party = Party().create_party(name, hqAddress, logoUrl)
        return make_response(jsonify({
            "msg": "Success"
        }),201)
    
    @pt_v1.route('/parties',methods =['GET'])
    def get_all_parties():
            parties=[]
            parties = Party().get_all()
            if parties:
                return make_response(jsonify({
                    'msg':'success',
                    'parties':parties
                }))
            return make_response(jsonify({
                'msg':'success',
                 'parties':parties
        }))                

    @pt_v1.route('/parties/<int:party_id>',methods =['GET'])
    def get_by_id(party_id):
            party = Party().get_party_by_id(party_id)   
            if party:
                return make_response(jsonify({
                    'msg':'success',
                    'parties':party
                    }))
            return make_response(jsonify({
                'msg':'NOt found'
                })) 

    @pt_v1.route('/parties', ,methods ='PUT')
    def edit_party(party_id):
        party = Party().edit_party(party_id)
        for myparty in party:
            if party.party_id =='party_id':
                myparty.update()
            return make_response(jsonify({
                'message':'update successful'
            }))

       
