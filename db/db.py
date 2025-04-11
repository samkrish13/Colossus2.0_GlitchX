
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='reverse_classroom_ai',
            user='your_mysql_username',
            password='your_mysql_password'
        )
        if connection.is_connected():
            print("✅ Connected to MySQL Database")
            return connection
    except Error as e:
        print(f"❌ Error: {e}")
        return None
