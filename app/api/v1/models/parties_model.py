
"""Initializing an empty list to hold our data"""
party_list = []


class Party():
    def __init__(self):
        self.party = party_list

    def create_party(self, name, hqAddress, logoUrl):
        party = {
            'party_id': len(self.party)+1,
            'name': name,
            'hqAddress': hqAddress,
            'logoUrl': logoUrl
        }
        self.party.append(party)
        return party

    def get_all(self):
        return self.party

    def get_party_by_id(self, party_id):
        if self.party:
            for party in self.party:
                if party.get('party_id') == party_id:
                    return party

    def edit_party(self):
        for party in party_list:
            if party:
                party.update['party_id']
            return party

    def delete_party(self, party_id):
        for party in party_list:
            if party in self.party:
                party_list.remove(party_id)
            return self.party
