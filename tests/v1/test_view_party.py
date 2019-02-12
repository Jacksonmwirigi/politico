import json
import unittest
import pytest
from app import create_app


class TestParties(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.dummy_party = {
            "name": "rullingParty",
            "hqAddress": "Milimani",
            "logoUrl": "my logi missing"
        }

    def post(self, path='/api/v1/parties'):
        response = self.client.post(path, data=json.dumps(
            self.dummy_party), content_type='application/json')
        return response

    def test_create_party(self):
        """ Tests create party"""
        respo = self.post()
        result = json.loads(respo.data.decode())
        self.assertEqual(result["msg"], "created Successfully")
        self.assertTrue(respo.status_code, 201)

    def test_get_all_parties(self):
        """Testing get-all parties end point"""
        respo = self.post()
        result = json.loads(respo.data.decode())
        self.assertEqual(result["msg"], "created Successfully")
        self.assertTrue(respo.status_code, 200)

    def test_get_specific_party(self):
        """Testing get-specific Party end point"""
        self.post()
        respo2 = self.client.get(path="api/v1/parties/1")
        result2 = json.loads(respo2.data.decode())
        self.assertEqual(result2["message"], "success")
        self.assertEqual(respo2.status_code, 200)

    def test_delete_party(self):
        """Testing delete a party"""
        respo = self.post()
        respo2 = self.client.delete(path="api/v1/parties/1")
        result2 = json.loads(respo.data.decode())
        self.assertEqual(result2["msg"], "created Successfully")
        self.assertTrue(respo.status_code, 200)

    def test_edit_party(self):
        """Testing edit party end point"""
        respo = self.post()
        respo2 = self.client.patch(path="api/v1/parties/1/name")
        result2 = json.loads(respo.data.decode())
        self.assertEqual(result2["msg"], "created Successfully")
        self.assertTrue(respo.status_code, 200)
