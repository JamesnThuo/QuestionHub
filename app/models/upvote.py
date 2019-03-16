"""Upvote Model Class"""
import datetime
import psycopg2
from .database import DatabaseConnection as db_conn

class Upvote(db_conn):
    def __init__(self,upvote_data):
        self.answer_id=upvote_data[0]
        self.user_id=upvote_data[1]

    def add_upvote(self,answer_id,user_id):
        """Adds an upvote to the database"""
        query="""INSERT INTO upvotes (answer_id,user_id) VALUES ('{}','{}')
        """.format(answer_id,user_id)
        self.saving_or_editing(query)
    
    def remove_upvote(self,answer_id,user_id):
        """Removes an upvote row from the database"""
        query=""" DELETE FROM upvotes WHERE answer_id = {} and user_id = {}
        """.format(answer_id,user_id)
        self.delete_row(query)