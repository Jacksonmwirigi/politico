from flask import Flask, make_response, request,jsonify
from flask import Blueprint
from app.api.v1.models.gov_offices_model import OfficeModel, offices


pt_v1 = Blueprint('v1', __name__, url_prefix='/api/v1/')
class OfficeView:
    def __init__(self):


    @pt_v1.route('/offices',methods = ['POST'])
    def create_office():
        data = request.get_json()
        name = data['name']
        candidate_id= data['candidate_id']
        date_created= data['date_created']
        OfficeModel().create_office(name,candidate_id,date_created)

        return make_response(jsonify({
            "msg":"Success"
        }),201)

