"""Tests for User Endpoints"""
import unittest
import os
import json
import psycopg2
from app import create_app
from instance.config import app_config
from app.models.database import DatabaseConnection

class UserTestCase(unittest.TestCase):
    """This class represents the user TestCase"""
    def setUp(self):
        """Defines the test variable"""
        pass
        # self.app=create_app("testing")
        # self.client=self.app.test_client()
        # self.userdata={
        #     "firstname":"James",
        #     "lastname":"Thuo",
        #     "email":"jamesnthuo@gmail.com",
        #     "password":"abcd" }
            
    def test_user_creation(self):
        """Test Api endpoint that add user"""
        # resp=self.client.post(path="/api/users/register", data=json.dumps(self.userdata), content_type="application/json")
        # self.assertEqual(resp.status_code, 201)
        pass

    def tearDown(self):
        """Teardown all initialized variables"""
        # with self.app.app_context():
            # DatabaseConnection.drop_tables(DatabaseConnection)
        pass