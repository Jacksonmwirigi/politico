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
    def get_all (self):
        return self.party  
  
    def get_party_by_id(self,party_id):
        if self.party:
            for party in self.party:
                if party.get('party_id') == party_id:      
                    return party
   def edit_party():
       if party in self.party in :
           if party.get('party_id')==party_id:
               new_party=update(self.party)
               self.party_list.update(party)
               return new_party
            

        


