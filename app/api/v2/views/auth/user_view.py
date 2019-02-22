from app.api.v2.models.user_model import UserModel
from app.api.v2.models.base_model import BaseModel
from flask import Flask,Blueprint ,make_response, jsonify, request
from flask.views import MethodView
from app.validation import*

register_bluprint =Blueprint("sign_up", __name__,url_prefix='/api/v2')
login_bluprint=Blueprint("login",__name__, url_prefix= '/api/v2')

@register_bluprint.route('/signup', methods=['POST'])
def register():
    """Registers new user entry into the database."""   
    key_error= is_register_key_correct(request)
    if key_error:
        return make_response(jsonify({
            "Error" :400,
            "msg" : "Invalid keys "
        })) 

    data= request.get_json()
    first_name=data['first_name']
    second_name=data['second_name']
    other_name=data['other_name']
    passport_url=data['passport_url']
    email_address=data['email_address']
    phone_number=data['phone_number']
    is_admin=data['is_admin']
    password=data['password']

    if isValidEmail(email_address)==False:
        return "Invalid email"
     
 
        
    new_user=UserModel(first_name,second_name,other_name,
                passport_url,email_address,phone_number,is_admin,password).register_user()
    
    if BaseModel().check_if_exists('users','email_address',email_address)==True :
        return make_response(jsonify({
            "error" :'This Email address Already exists',
            "status":409
        })) 

    if new_user:
        token =BaseModel().encode_auth_token( email_address)
    else :
        return make_response(jsonify({
            "Error" :404,
            "msg" : "No data provided"
    }))   

    return make_response(jsonify({
        'status': 201,
        'message': 'Successfully registered.',
        'data': new_user,
        'token' : token.decode()
    }),201)

@register_bluprint.route('/signup', methods=['GET'])
def view_users():
    """retrieves all the registered users in the db. only requires admin previleges"""
    users= UserModel.get_all_users()
    if users:
        return make_response(jsonify({
            'status': 200,
            'message': 'Successful',
            'data': users
            
        }),200)
    return make_response(jsonify({
        'status': 404,
        'message': 'User not registred'

    }),404)    

@login_bluprint.route('/login', methods= ['POST'])
def user_signIn():
    """This end point allows regietered users to log in the system"""
    data= request.get_json()
    email_address =data['email_address']

    user= UserModel.get_email_address(email_address)
    if user:
        token =BaseModel().encode_auth_token(email_address)
        return make_response(jsonify({
            "status": 200,
            "msg": "Sign In successful",
            "data" : user,
            "token": token.decode()
        }),200)
    return make_response(jsonify({
        "error" :404,
        "msg" : "Email not registered"
    }),404)   
