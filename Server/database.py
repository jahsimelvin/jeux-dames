import mysql.connector
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Erreur de connexion : {err}")
        return None
