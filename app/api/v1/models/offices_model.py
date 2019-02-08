from flask import Flask, json, make_response

"""defining my list as a global variable"""
offices = []


"""This class will handle all the government office operations"""


class OfficeModel:
    def __init__(self):
        self.office = offices

    def create_office(self,name, candidate_id, date_created):
        new_office= {
            'office_id': len(self.office)+1,
            'name': name,
            'candidate_id': candidate_id,
            'date_created': date_created
          }

        self.office.append(new_office)
        return new_office

    """this function defines model for the get specific office end point."""
    def get_office_by_id(self, office_id):
        if self.office:
            for office in self.office:
                if office.get('office_id') == office_id:

                    return office   

    """get_all retrieves all the registered gov offices from the system"""
    def get_all(self):
        return self.office   

    
    def edit_office(self, office_id, data):
        for office in offices:
            """defines arguments for edit office route/ end point"""
            if office('party_id') == office_id:
                name = data.get("name")
            if name:
                office["name"] = name
            return office


    def if_office_exists(self, office_id):
        """this method checks if a government office exists before delete request"""
        for office in self.office:
            if office['party_id'] == office_id:
                return office
            else:
                return None

    """THis function deletes an existing office"""
    def delete_office(self, office_id):
        for office in offices:
            if office in self.office:
                offices.remove(office)
            return "delete successful"    
                                           
