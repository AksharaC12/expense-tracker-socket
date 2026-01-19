import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # change if needed
        password="password",   # change if needed
        database="expense_tracker"
    )
