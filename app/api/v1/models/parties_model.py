
"""Initializing an empty list to hold our data"""
party_list = []


class Party:
    def __init__(self):
        """Initializing class instance variables"""
        self.party = party_list

    """This function creates a new political party   """

    def create_party(self, name, hqAddress, logoUrl):
        party = {
            'party_id': len(self.party)+1,
            'name': name,
            'hqAddress': hqAddress,
            'logoUrl': logoUrl
        }
        self.party.append(party)
        return party


