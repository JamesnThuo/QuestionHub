"""Test for question Endpoints"""
import unittest
import os
import json
import psycopg2

from app import create_app
from app.models.database import DatabaseConnection
from instance.config import app_config
class QuestionTestCase(unittest.TestCase):
    """This class represents the question testcase"""
    def setUp(self):
        """Defines the test variables and initialize app"""
        self.app=create_app("testing")
        self.client=self.app.test_client()
        self.question={"description":"What is the square root of 4","user_id":1}
    
    def test_question_creation(self):
        """Test Api that can add question"""
        resp=self.client.post(path='/api/questions', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(resp.status_code, 201)
        # self.assertIn('What is the square root of 4', str(resp.data))

    def tearDown(self):
        """Teardown all initialized variables"""
        with self.app.app_context():
            DatabaseConnection.drop_tables(DatabaseConnection)
        pass

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()