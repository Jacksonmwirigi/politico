import json
import unittest
import pytest
from app import create_app

class TestParties(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.dummy_party = {
            "name": "rullingParty",
            "hqAddress": "Milimani",
            "logoUrl": "mylogo.jpeg"
        }
        self.dummy_editParty ={
            "name": "Changed party",
            "hqAddress": "New location",
            "logoUrl": "msoon added"
        }
        self.dummy_wrong ={
            "name":"fhh ",
            "fakeAdres" :"EEG",
            "imag":"12/02/2018"
        }

    def post(self, path='/api/v1/parties'):
        response = self.client.post(path, data=json.dumps(
            self.dummy_party), content_type='application/json')
        return response

    def post_wrong(self, path='/api/v1/parties'):
        res = self.client.post(path, data=json.dumps(
            self.dummy_wrong), content_type='application/json')
        return res   

    def test_create_party(self):
        """ Tests create party"""
        respo = self.post()
        result = json.loads(respo.data.decode())
        self.assertEqual(result["msg"], "created Successfully")
        self.assertTrue(respo.status_code, 201)

    def test_if_party_key_incorrect(self):
        res = self.post_wrong()  
        result = json.loads(res.data.decode())
        self.assertEqual(result["msg"], "Invalid keys used")
        self.assertTrue(res.status_code, 400)

    def test_get_all_parties(self):
        """Testing get-all parties end point"""
        respo = self.post()
        respo2 = self.client.get(path="api/v1/parties")
        result = json.loads(respo2.data.decode())
        self.assertEqual(result["msg"], "success")
        self.assertTrue(respo.status_code, 200)

    def test_get_specific_party(self):
        """Testing get-specific Party end point"""
        self.post()
        respo2 = self.client.get(path="api/v1/parties/1")
        result2 = json.loads(respo2.data.decode())
        self.assertEqual(result2["message"], "success")
        self.assertTrue(respo2.status_code, 200)

    def test_delete_party(self):
        """Testing delete a party"""
        # respo = self.post()
        respo2 = self.client.delete(path="api/v1/parties/1")
        result2 = json.loads(respo2.data.decode())
        self.assertEqual(result2['message'], "Deleted successfully")
        self.assertEqual(respo2.status_code, 200)

    def test_edit_party(self):
        """Testing edit party end point"""
        respo = self.post()
        #respo2 = self.client.patch(path="api/v1/parties/1")
        edit_response= self.client.patch(path= "api/v1/parties/1", data=json.dumps(
            self.dummy_editParty), content_type='application/json')
        result2 = json.loads(edit_response.data.decode())
        self.assertEqual(result2["message"], "update successful")
        self.assertEqual(respo.status_code, 201)
