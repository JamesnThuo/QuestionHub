"""Answer Model"""
import psycopg2
import datetime
from .database import DatabaseConnection as db_url

time_now=datetime.datetime.utcnow()

class Answer(db_url):
    def __init__(self,answer_data,isCorrect=False):
        self.description=answer_data[0]
        self.question_id=answer_data[1]
        self.postedOn=time_now
        self.isCorrect=isCorrect
    
    def add_answer(self):
        """inserts an answer in teh database"""
        query=""" INSERT INTO answers (description,question_id,postedOn, isCorrect) VALUES ('{}','{}','{}','{}');
        """.format(self.description,self.question_id,self.postedOn,self.isCorrect)
        self.saving_or_editing(query)
    
    def delete_answer(self, answer_id):
        """Deletes and answer from the database"""
        query=""" DELETE FROM answers WHERE id = {} """ .format(answer_id)
        self.delete_row(query)
    
    def select_correct_answer(self, answer_id, question_id):
        """Allows the owner of the question to select correct answer"""
        query=""" UPDATE ansers SET isCorrect = True WHERE question_id= {}""".format(question_id)
        self.saving_or_editing(query)