"""Question Model"""
import datetime
import psycopg2
from .database import DatabaseConnection as db_conn

time_now=datetime.datetime.utcnow()

class Question(db_conn):
    def __init__(self,question_data):
        self.description=question_data[0]
        self.user_id=question_data[1]
        self.posted_on=time_now
    
    def add_question(self):
        """Adding a question to database"""
        query="""INSERT INTO questions (description,user_id,postedon) VALUES ('{}','{}','{}')
        """.format(self.description,self.user_id,self.posted_on)
        self.saving_or_editing(query)
    
    def delete_question(self, question_id):
        """Deleting a question from the database"""
        query="""DELETE FROM questions WHERE questions.id = {}""".format(question_id)
        self.delete_row(query)