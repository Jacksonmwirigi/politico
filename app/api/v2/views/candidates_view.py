from app.api.v2.models.candidate_model import Candidates
from app.api.v2.models.base_model import BaseModel
from flask import Flask,Blueprint ,make_response, jsonify, request
from flask.views import MethodView
from app.validation import*

def register_candidate():

    data =request.get_json()
    user_id=data['user_id']
    office_id=data['office_id']
    party_id=data['party_id']
    date_created=data['date_created']
    
    