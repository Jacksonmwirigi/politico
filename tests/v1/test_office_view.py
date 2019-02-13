import json
import unittest
import pytest
from app import create_app


class TestOffices(unittest.TestCase):
    """Test case for the office end points"""

    def setUp(self):
        """Setting up a test client"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.dummy_office = {
            "office_name": "Office of the President",
            "office_type" : "Executive"
        }
        self.dummy_invalid ={
            "wrongname":"fhh ",
            "fakeofficetp" :"EEG"
         
        }

    def post(self, path='/api/v1/offices'):
        response = self.client.post(
            path="/api/v1/offices", data=json.dumps(self.dummy_office), content_type='application/json')
        return response

    def post_wrong(self, path='/api/v1/offices'):
        res = self.client.post(path, data=json.dumps(
            self.dummy_invalid), content_type='application/json')
        return res   
 

    def test_create_office(self):
        """ Tests create party end point """
        respo = self.post()
        result = json.loads(respo.data.decode())
        self.assertEqual(result["msg"], "success")
        self.assertTrue(respo.status_code, 201)

    def test_if_office_key_incorrect(self):
        res = self.post_wrong()  
        result = json.loads(res.data.decode())
        self.assertEqual(result["msg"], "Invalid keys used")
        self.assertTrue(res.status_code, 400)

    def test_get_all_offices(self):
        """testing get-all offices end point"""
        respo = self.post()
        result = json.loads(respo.data.decode())
        self.assertEqual(result["msg"], "success")
        self.assertTrue(respo.status_code, 200)

    def test_get_specific_office(self):
        """Testing get-specific office end point"""
        respo = self.post()
        respo2 = self.client.get(path="/api/v1/offices/1")
        result2 = json.loads(respo2.data.decode())
        self.assertEqual(result2["msg"], "success")
        self.assertTrue(respo.status_code, 200)
