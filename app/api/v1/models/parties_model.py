
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

    def edit_party(self, party_id, data):
        for party in party_list:
            if party('party_id') == party_id:

                name = data.get("name")
                hqAddress = data.get("hqAddress") 
                logoUrl=data.get("logUrl")
            if name:
                party["name"] = name
            if hqAddress:
                party["hqAddress"] = hqAddress
            if logoUrl:  
                party["logoUrl"] = logoUrl           

            return party    


