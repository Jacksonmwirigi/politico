import json
import unittest
import pytest
from app import create_app
from app.api.v1.views.office_views import OfficeView


class TestOffices(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.dummy_office = {
            "name": "rullingParty",
            "candidate_id": "Milimani",
            "date_created": "2/02/2018"
        }

    def post(self, path='/api/v2/offices'):
        response = self.client.post(
            path="/api/v2/offices", data=json.dumps(self.dummy_office), content_type='application/json')
        return response

    def test_create_office(self):
        """ Tests create party"""
        respo = self.post()
        result = json.loads(respo.data.decode())
        self.assertEqual(result["msg"], "success")
        self.assertTrue(respo.status_code, 201)

    def test_get_all_offices(self):
        respo = self.post()
        result = json.loads(respo.data.decode())
        self.assertEqual(result["msg"], "success")
        self.assertTrue(respo.status_code, 200)

    def test_get_specific_party(self):
        respo = self.post()
        result = json.loads(respo.data.decode())
        respo2 = self.client.post(path="/api/v2/offices{}office_id", data=json.dumps(
            self.dummy_office), content_type='application/json')
        result2 = json.loads(respo.data.decode())
        self.assertEqual(result2["msg"], "success")
        self.assertTrue(respo.status_code, 200)

    def test_delete_party(self):
        respo = self.post()
        result = json.loads(respo.data.decode())
        respo2 = self.client.post(path="/api/v2/offices{}office_id", data=json.dumps(
            self.dummy_office), content_type='application/json')
        result2 = json.loads(respo.data.decode())
        self.assertEqual(result2["msg"], "success")
        self.assertTrue(respo.status_code, 200)

    def test_edit_party(self):
        respo = self.post()
        result = json.loads(respo.data.decode())
        respo2 = self.client.post(path="api/v1/parties{}party_id/name",
                                  data=json.dumps(self.dummy_office), content_type='application/json')
        result2 = json.loads(respo.data.decode())
        self.assertEqual(result2["msg"], "success")
        self.assertTrue(respo.status_code, 200)
