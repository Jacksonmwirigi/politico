
"""Initializing an empty list to hold our data"""
party_list = []


class Party:
    def __init__(self):
        """Initializing class instance variables"""
        self.party = party_list

    """This function creates a new  party object  """

    def create_party(self, name, hqAddress, logoUrl):
        party = {
            'party_id': len(self.party)+1,
            'name': name,
            'hqAddress': hqAddress,
            'logoUrl': logoUrl
        }
        self.party.append(party)
        return party

   """This is the route allows user to retrieve one political party with specific party id"""

    @pt_v1.route('/parties/<int:party_id>', methods=['GET'])
    def get_by_id( party_id):

        party = Party().get_party_by_id(party_id)
        if party:

            return make_response(jsonify({
            'msg': 'success',
            'parties': party
            }))
        return make_response(jsonify({
        'msg': 'NOt found'
        }))
