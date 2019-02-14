from flask import Flask,Blueprint, jsonify, make_response, request
from app.api.v2.models.user_model import UserModel
from app.api.v2.models.base_model import BaseModel

register_bluprint =Blueprint("sign_up", __name__,url_prefix='/api/v2')

@register_bluprint.route('/signup', methods=['POST'])
def post_new():
    post_data = request.get_json()
    if post_data:
       
        first_name=post_data['first_name']
        second_name=post_data['second_name']
        other_name=post_data['other_name']
        email=post_data.get['email']
        phone_number=post_data['phone_number']
        passportUrl=post_data['passportUrl']
        isAdmin=post_data['isAdmin']
        isCandidate=post_data['isCandidate']
        
        respo= UserModel().register_new(first_name,second_name,other_name,email,
        phone_number,passportUrl,isAdmin,isCandidate)
        

        
        # auth_token = user.encode_auth_token(user_id)
        # responseObject = {
        #     'status': 200,
        #     'message': 'Successfully registered.',
        #     'auth_token': auth_token.decode()
        # }
        
        return make_response(jsonify({
            'status': 'success',
            'message': 'Successfully registered.',
            'auth_token': post_data
        }),201)
    return make_response(jsonify({
        'status': 'success',
        'message': 'Successfully registered.',
        'auth_token': post_data
    }))
            

            
    
    
    # if BaseModel().check_if_exists('users', 'passportUrl',passportUrl) ==False :          
    #     try:
            # new_user = {
            #     first_name=post_data.get('first_name'),
            #     second_name=post_data.get('second_name'),
            #     other_name=post_data.get('other_name'),
            #     email=post_data.get('email'),
            #     phone_number=post_data.get('phone_number'),
            #     passportUrl=post_data.get('passportUrl'),
            #     isAdmin=post_data.get('isAdmin'),
            #     isCandidate=post_data.get('isCandidate')
            # }

    #         respo= UserModel(new_user)

        
    #         # insert the user
    #         UserModel().register_new( user)
    #         # db.session.commit()
    #         # generate the auth token
    #         auth_token = user.encode_auth_token(user_id)
    #         responseObject = {
    #             'status': 'success',
    #             'message': 'Successfully registered.',
    #             'auth_token': auth_token.decode()
    #         }
    #         return make_response(jsonify(responseObject)), 201
    #     except Exception as e:
    #         responseObject = {
    #             'status': 'fail',
    #             'message': 'Some error occurred. Please try again.'
    #         }
    #         return make_response(jsonify(responseObject)), 401
    # else:
    #     responseObject = {
    #         'status': 'fail',
    #         'message': 'User already exists.',
    #     }
    