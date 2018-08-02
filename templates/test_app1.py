import unittest
import dbconnection
from app1 import app
import json
import validator
import pytest


class TestEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = app.test_client()
        self.app.testing = True
        self.conn = dbconnection.connection()
        self.user = {
            "username":"TestUser",
            "email":"test@mail.com",
            "password":"testpass"
        }
        self.entry = {
            "title":"Test entry",
            "content":"Test content"
        }

        self.signin = {
            "email":"test@mail.com",
            "password":"testpass"
        }
    def test_register_user(self):
        """status code for get one should be ok: 200 where id passed is valid """
        with app.test_request_context():
            resp = self.client.post("/mydiary/v1/auth/sgnup",
                                    data=self.user,
                                    content_type="application/json")
            assert resp.status_code, 200

    def test_sign_in(self):
        """status code for signin """
        resp = self.client.post("/mydiary/v1/auth/signup",
                                data=self.signin,
                                content_type="application/json")
        assert resp.status_code, 200

    

# T=TestEndpoint()
# T.setUp()
    




