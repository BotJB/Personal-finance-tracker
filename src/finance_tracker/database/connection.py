"""
This class is to create the database connection
"""

import mysql.connector
from mysql.connector import Error

import os 
from dotenv import load_dotenv

load_dotenv()

class DataBaseConnection:
    def __init__(self):
        self.host=os.getenv('DB_HOST')
        self.port=os.getenv('DB_PORT')
        self.database=os.getenv('DB_NAME')
        self.user=os.getenv('DB_USER')
        self.password=os.getenv('DB_PASSWORD')
        self.connection=None

    def connect(self):
        try:
            self.connection=mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print('Connected to the database')
                return True
        except Error as e:
            print('Cannot connect to the database')
            return False

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection has been closed")

    def execute_query(self, query, params=None):
     try:
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params or ())
        results = cursor.fetchall()
        cursor.close()
        return results
     except Error as e:
        print(f"Error executing query: {e}")
        return None        

def test_connection():
     db = DataBaseConnection()
     if db.connect():
        # Test with a simple query
        accounts = db.execute_query("SELECT * FROM accounts LIMIT 3")
        if accounts:
            print("\n📊 Sample accounts:")
            for account in accounts:
                print(f"  - {account['name']}: ${account['current_balance']}")
        db.disconnect()
        return True
     return False


