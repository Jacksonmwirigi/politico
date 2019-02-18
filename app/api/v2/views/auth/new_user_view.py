from app.api.v2.models.new_user_model import UserModeln
from flask import Flask,Blueprint ,make_response, jsonify, request

register_bluprint =Blueprint("sign_up", __name__,url_prefix='/api/v2')
@register_bluprint.route('/signup', methods=['POST'])
def register():

    data= request.get_json()
    first_name=data['first_name']
    second_name=data['second_name']
    other_name=data['other_name']
    passport_url=data['passport_url']
    email_address=data['email_address']
    phone_number=data['phone_number']
    is_admin=data['is_admin']

   
    new_user=UserModeln(first_name,second_name,other_name, passport_url,email_address,phone_number,is_admin).register_user()
    # result =UserModeln.register_user(new_user)
    token =UserModeln().encode_auth_token(new_user.email_address)


    return make_response(jsonify({
        'status': 201,
        'message': 'Successfully registered.',
        'data': new_user,
        'token' : 'token'
    }),201)


@register_bluprint.route('/signup', methods=['GET'])
def view_users():
    users= UserModeln().get_all_users()

    return make_response(jsonify({
        'status': 200,
        'message': 'Successfully registered.',
        'data': users

    }),200)
        


