
"""Initializing an empty list to hold our data"""
party_list = []


class Party:
    def __init__(self):
        """Initializing class instance variables"""
        self.party = party_list

    """This function creates a new political party   """
 
    def create_party(self,name,hqAddress, logoUrl ):
        party = {
            'party_id': len(self.party)+1,
            'name': name,
            'hqAddress': hqAddress,
            'logoUrl': logoUrl
        }
        self.party.append(party)
        return party

    """get_all retrieves all the registered parties from , in this case, my party_list"""

    def get_all(self):
        return self.party

    def get_party_by_id(self, party_id):
        if self.party:
            for party in self.party:
                if party.get('party_id') == party_id:

                    return party

    """defines arguments for edit party route/ end point"""
    def edit_party(self, party_id, data):
        for party in party:
            if party('party_id') == party_id:
                name = data.get("name")
            if name:
                party["name"] = name
            return party

    def delete_party(self, party_id):
        for party in party_list:
            if party in self.party:
                party_list.remove(party)
