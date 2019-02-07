import json
import unittest
from app import create_app

class TestParties(unittest.TestCase):
    def setUp(self):
        self.app =create_app()
        self.client = self.app.test_client()
        self.data = {
            "name" : "rullingParty" ,
            "hqAddress" :"Milimani" ,
            "logoUrl" : "my logi missing"
        }


    def post(self, path = '/parties' , data={}):
        if not data:
            data=self.data

        respo= self.client.post(path='api/vi/parties',data=json.dumps(self.data),content_type='application/json')
        return respo

    def test_create_party(self):
        respo=self.post()
        self.assertEqual(respo.status_code, 201)
        self.assertTrue(respo.json('party_id'))
        self.assertEqual(['msg'],'Created Successfully')

    def test_get_all_parties(self):
        respo= self.client.get(path = '/parties', content_type= 'application/json')
        self.assertEqual(respo.status_code,200) 
