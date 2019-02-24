from app.api.v2.models.party_model import Parties
from app.api.v2.models.base_model import BaseModel
from flask import Flask,Blueprint ,make_response, jsonify, request
from flask.views import MethodView
from app.validation import*

party_bluprint =Blueprint("parties", __name__,url_prefix='/api/v2')
@party_bluprint.route('/parties',methods=['POST'])
def post_party():
    data =request.get_json()
    if data:
        party_name=data['party_name']
        hq_address=data['hq_address']
        logo_url=data['logo_url']

    if BaseModel().check_if_exists('parties','party_name',party_name):
        return make_response(jsonify({
            "error":409,
            "msg" :"name already registered"

        }))    

    nw_party= Parties(party_name,hq_address,logo_url).register_party()
    return make_response(jsonify({
        "status":201,
        "data" :nw_party,
        "msg" :"success"
    }))

@party_bluprint.route('parties',methods=['GET'])
def view_parties():
    parties=Parties.view_all_parties()
    return make_response(jsonify({
        "status":200,
        "msg" :"success",
        "data" : parties
    }))

