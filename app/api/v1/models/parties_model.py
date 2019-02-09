
"""Initializing an empty list to hold our data"""
PARTY_LIST = []


class Party:
    def __init__(self):
        """defining class instance variables"""
        self.party = PARTY_LIST

    def create_party(self, name, hqAddress, logoUrl):
        """Defining create a new political party function"""
        party = {
            'party_id': len(self.party)+1,
            'name': name,
            'hqAddress': hqAddress,
            'logoUrl': logoUrl}
        PARTY_LIST.append(party)
        return party

    def get_all(self):
        """get_all retrieves all the registered parties from , in this case, my party_list"""
        return self.party

    def get_party_by_id(self, party_id):
        if self.party:
            for party in self.party:
                if party.get('party_id') == party_id:

                    return party

    def edit_party(self, party_id, data):
        for party in party:
            """defines arguments for edit party route/ end point"""
            if party('party_id') == party_id:
                name = data.get("name")
            if name:
                party["name"] = name
            return party

    def if_party_exists(self, party_id):
        """this method checks if a party exists before delete"""
        for party in self.party:
            if party['party_id'] == party_id:
                return party
            else:
                return None

    def delete_party(self, party_id):
        """defining delete party """
        for party in PARTY_LIST:
            if party in self.party:
                PARTY_LIST.remove(party)
            return "delete successful"
