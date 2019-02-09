from flask import Flask, make_response, request, jsonify
from flask import Blueprint
from app.api.v1.models.offices_model import OfficeModel

pt_v2 = Blueprint('v2', __name__, url_prefix='/api/v2')


class OfficeView():
    """defining all the end points """

    @pt_v2.route('/offices', methods=['POST'])
    def create_office():
        """create office end point"""
        data = request.get_json()
        name = data['name']
        candidate_id = data['candidate_id']
        date_created = data['date_created']
        OfficeModel().create_office(name, candidate_id, date_created)
        return make_response(jsonify({
            "msg": "success"
        }), 201)
   
    @pt_v2.route('/offices/<int:office_id>', methods=['GET'])
    def get_by_id(office_id):
        """This is the route allows user to retrieve one 
        specific government opffice by specifying the office id"""
        office = OfficeModel().get_office_by_id(office_id)
        if office:
            return make_response(jsonify({
                'msg': 'success',
                'office': office
            }))
        return make_response(jsonify({
            'msg': 'NOt found'
        }))
    @pt_v2.route('/offices', methods=['GET'])
    def get_all_offices(self):
        """This is the route for retrieving all government ofices."""
        offices = OfficeModel().get_all()
        if offices:
            return make_response(jsonify({
                'msg': 'success',
                'offices': offices
            }))
        return make_response(jsonify({
            'msg': 'success',
            'offices': offices
        }))

       
    @pt_v2.route('/offices/<int:office_id>/name', methods=['PUT'])
    def edit_office(office_id):
        """ End point for editing office by sending a PUT request on postman"""
        data = request.get_json
        office = OfficeModel().edit_office(office_id, data)
        return make_response(jsonify({
            'status': 'OK',
            'message': 'update successful',
            'offices': office
            }), 200)


    """delete office end point"""
    @pt_v2.route('/offices/<office_id>', methods=['DELETE'])
    def delete_a_office(office_id):
        """This method checks for an existing office then deletes it """
        office = OfficeModel().if_office_exists(office_id)
        if office:
            office_res =OfficeModel().delete_office(office)
            
            return make_response(jsonify({
                'status': 200, 
                'message': "Deleted successfully"
                }), 200)
        else:    
            return make_response(jsonify({
                'status': 404,
                'message': 'office does not exist'
            }), 404)    
