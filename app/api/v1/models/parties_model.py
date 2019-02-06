
"""Initializing an empty list to hold our data"""
party_list = []


class Party:
    def __init__(self):
        """Initializing class instance variables"""
        self.party = party_list

    """This function creates a new  party object  """

    def create_party(self,name,hqAddress,logoUrl):
        party = {
            'party_id': len(self.party)+1,
            'name': name,
            'hqAddress':hqAddress,
            'logoUrl': logoUrl
        }
        self.party.append(party)
        return party

    """get_all retrieves all the registered parties from , in this case, my party_list"""

    def get_all(self):
        return self.party
