from flask import Flask, json, make_response

"""defining my list as a global variable"""
offices = []


"""This class will handle all the government office operations"""


class OfficeModel:
    def __init__(self, name, candidate_id, date_created):
        self.office=offices
        self.name = name
        self.candidate_id = candidate_id
        self.date_created = date_created

    def create_office(self):
        office= [
        {
            'office_id': len(self.office)+1,
            'name': self.name,
            'candidate_id': self.candidate_id,
            'date_created': self.date_created
        }]

        offices.append(office)
        return office

    """this function defines model for the get specific office end point."""
    def get_office_by_id(self, name):
        if self.office:
            for office in self.office:
                if office.get('name') == name:

                    return office   

    """get_all retrieves all the registered gov offices from the system"""
    def get_all(self):
        return self.office                              
