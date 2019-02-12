"""defining my list as a global variable"""
OFFICES = []
class OfficeModel:
    """This class will handle all the government office operations"""

    def __init__(self):
        self.office = OFFICES

    def create_office(self, name, candidate_id, date_created):
        """Defining create office data representation"""
        new_office = {
            'office_id': len(self.office)+1,
            'name': name,
            'candidate_id': candidate_id,
            'date_created': date_created
        }
        self.office.append(new_office)
        return new_office

    def get_office_by_id(self, office_id):
        """this function defines model for the get specific office end point."""
        if self.office:
            office_item = [
                office for office in OFFICES if office['office_id'] == office_id]
            return office_item

    def get_all(self):
        """get_all retrieves all the registered gov offices from the system"""
        return self.office
