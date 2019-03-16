import os
import datetime
from .database import DatabaseConnection as db_url

time_now=datetime.datetime.utcnow()

class Answer(db_url):
    def __init__(self,answer_data,isCorrect=False):
        self.description=answer_data[0]
        self.user_id=answer_data[1]
        self.question_id=answer_data[2]
        self.postedOn=time_now
        self.isCorrect=isCorrect
    
    def add_answer(self,answer_data):
        """inserts an answer in teh database"""
        query=""" INSERT INTO ansWers (description, user_id ,question_id,postedOn, isCorrect) VALUES ('{}','{}','{}','{}','{}');
        """.format(self.description,self.user_id,self.question_id,self.postedOn,self.isCorrect)
        self.saving_or_editing(query)
    
    def delete_answer(self, answer_id):
        """Deletes and answer from the database"""
        query=""" DELETE FROM answers WHERE id = {} """ .format(answer_id)
        self.delete_row(query)
    
    