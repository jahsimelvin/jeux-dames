# models.py
import mysql.connector
from database import connect_to_database

def create_user(nom, email, mot_de_passe):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "INSERT INTO utilisateur (nom, email, mot_de_passe) VALUES (%s, %s, %s)"
    cursor.execute(query, (nom, email, mot_de_passe))

    connection.commit()
    cursor.close()
    connection.close()

def get_user_by_email(email):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT * FROM utilisateur WHERE email = %s"
    cursor.execute(query, (email,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()
    return result

def create_game(joueur1_id, joueur2_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "INSERT INTO historique_partie (joueur1_id, joueur2_id) VALUES (%s, %s)"
    cursor.execute(query, (joueur1_id, joueur2_id))

    connection.commit()
    cursor.close()
    connection.close()

def get_game_by_id(game_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    query = "SELECT * FROM historique_partie WHERE id = %s"
    cursor.execute(query, (game_id,))
    result = cursor.fetchone()

    cursor.close()
    connection.close()
    return result
