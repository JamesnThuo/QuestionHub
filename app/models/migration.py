import os
import datetime

def drop_table_if_exists():
    """ Deletes all tables"""
    drop_users = """ DROP TABLE IF EXISTS users """
    drop_questions = """ DROP TABLE IF EXISTS questions """
    drop_answers= """ DROP TABLE IF EXISTS answers """
    drop_upvotes= """ DROP TABLE IF EXISTS upvote """
    return [drop_questions, drop_users, drop_answers, drop_upvotes]

def set_up_tables():
    """Setting up the database schema"""
    create_users_table=""" CREATE TABLE IF NOT EXISTS users (
            id serial PRIMARY KEY,
            firstname VARCHAR(50) NOT NULL,
            lastname VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL,
            registerdate TIMESTAMP
        ); """
    create_questions_table="""CREATE TABLE IF NOT EXISTS questions (
            id serial PRIMARY KEY,
            description VARCHAR(50),
            postedOn TIMESTAMP,
            user_id INT
        );"""
    create_answer_table="""CREATE TABLE IF NOT EXISTS answers (
            id serial PRIMARY KEY,
            description VARCHAR(50),
            user_id INT,
            question_id INT,
            postedOn TIMESTAMP,
            isCorrect BOOLEAN DEFAULT FALSE
        );"""
    create_upvote_table="""CREATE TABLE IF NOT EXISTS upvote (
            answer_id INT,
            user_id INT
        );"""
    
    return [create_users_table,create_questions_table,create_answer_table,create_upvote_table]



