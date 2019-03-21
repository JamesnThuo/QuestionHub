import unittest
import os
import json
import psycopg2
from app import create_app
from instance.config import app_config

class AnswerTestCase(unittest.TestCase):
    def setUp(self):
        self.app=create_app("testing")
        self.client=self.app.test_client()
    
    def testaddanswer(self):
        pass
    
    def tearDown(self):
        with self.app.app_context():
            pass