import json
import unittest
import pytest
from app import create_app

class TestParties(unittest.TestCase):

    def setUp(self):
        self.app =create_app()
        self.client =self.app.test_client()
        self.dummy_party= {
            "name" : "rullingParty" ,
            "hqAddress" :"Milimani" ,
            "logoUrl" : "my logi missing"
        }
    def post(self, path = 'api/v1/parties' ):
        response= self.client.post(path='api/vi/parties',data=json.dumps(self.dummy_party),content_type='application/json')
        return response

    def test_create_party(self):
        """ Tests create party"""
        respo = self.post()
        self.assertTrue(respo.status_code, 201)

    def test_get_all_parties(self):
        respo = self.post() 
        self.assertTrue(respo.status_code,200)

    def test_get_specific_party(self):    
        respo = self.post()
        self.assertTrue(respo.status_code, 200)
