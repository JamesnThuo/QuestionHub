"""Upvote mode"""
import psycopg2
from .database import DatabaseConnection as db_conn

class Upvote(db_conn):
    def __init__(self,upvote_data):
        self.answer_id=upvote_data[0]
        self.user_id=upvote_data[1]
    
    def add_upvote(self):
        query=""" INSERT INTO upvote (answer_id, user_id) VALUES ('{}','{}')
        """.format(self.answer_id,self.user_id)
        self.saving_or_editing(query)