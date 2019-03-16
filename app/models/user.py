"""User model"""
import datetime
import psycopg2
from .database import DatabaseConnection as db_conn

time_now=datetime.datetime.utcnow()

class User(db_conn):
    def __init__(self, userdata):
        self.firstname=userdata[0]
        self.secondname=userdata[1]
        self.email=userdata[2]
        self.password=userdata[3]
        self.registerdate=time_now

    """Registering a new user"""
    def create_new_user(self):
        query=""" INSERT INTO users (firstname, secondname, email, password, registerdate) VALUES ('{}','{}','{}','{}','{}')
        """ .format(self.firstname,self.secondname,self.email,self.password,self.registerdate)
        
        """passing to database function to save user"""
        self.saving_or_editing(query)
        

