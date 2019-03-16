import psycopg2
from .migration import set_up_tables, drop_table_if_exists

class DatabaseConnection:
    """Handles the main connection to the database of the app setting"""
    def __init__(self,db_url):
        """"Initialize the class intance to take a database url as a parameter"""
        try:
            global conn,cur

            #connection
            conn=psycopg2.connect(db_url)
            cur=conn.cursor()
        except Exception as error:
            print(error)
    
    def create_tables(self):
        """creating the tables in migration"""
        tables_to_create=set_up_tables()
        for query in tables_to_create:
            cur.execute(query)
            conn.commit()
    
    def drop_tables(self):
        """Drops tables in the database"""
        tables_to_drop=drop_table_if_exists()
        for query in tables_to_drop:
            cur.execute(query)
            conn.commit()
    
    def fetch_single_row(self,query):
        """Fetches a single row in a table"""
        cur.execute(query)
        fetchedRow=cur.fetchone()
        return fetchedRow
    
    def saving_or_editing(self,query):
        """Saves or edits data in the database"""
        cur.execute(query)
        conn.commit()
    
    def fetch_all_rows(self,query):
        """Fetches all rows in a table"""
        cur.execute(query)
        all_rows=cur.fetchall()
        return all_rows
    
    def delete_row(self,query):
        """Deletes a row in a table"""
        cur.execute(query)
        conn.commit()