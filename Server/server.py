# server.py
import socket
import threading
from models import create_user, get_user_by_email, create_game, get_game_by_id
from game import Game
from config import SECRET_KEY
import hashlib

# Fonction de gestion des connexions utilisateurs
def handle_client(client_socket, addr):
    print(f"Nouvelle connexion depuis {addr}")

    try:
        # Exemple simple : Demander à l'utilisateur de se connecter ou de s'inscrire
        client_socket.send(b"Bienvenue! Tapez '1' pour vous inscrire ou '2' pour vous connecter.\n")

        option = client_socket.recv(1024).decode('utf-8')

        if option == '1':  # Inscription
            client_socket.send(b"Entrez votre nom: ")
            nom = client_socket.recv(1024).decode('utf-8')
            client_socket.send(b"Entrez votre email: ")
            email = client_socket.recv(1024).decode('utf-8')
            client_socket.send(b"Entrez votre mot de passe: ")
            mot_de_passe = client_socket.recv(1024).decode('utf-8')
            mot_de_passe_hash = hashlib.sha256(mot_de_passe.encode()).hexdigest()  # Hachage du mot de passe

            create_user(nom, email, mot_de_passe_hash)
            client_socket.send("Inscription réussie!\n".encode('utf-8'))

        elif option == '2':  # Connexion
            client_socket.send(b"Entrez votre email: ")
            email = client_socket.recv(1024).decode('utf-8')
            client_socket.send(b"Entrez votre mot de passe: ")
            mot_de_passe = client_socket.recv(1024).decode('utf-8')
            mot_de_passe_hash = hashlib.sha256(mot_de_passe.encode()).hexdigest()

            user = get_user_by_email(email)
            if user and user[3] == mot_de_passe_hash:
                client_socket.send("Connexion réussie!\n".encode('utf-8'))
            else:
                client_socket.send(b"Email ou mot de passe incorrect.\n")
                client_socket.close()
                return

        # Après la connexion, gérer la partie
        client_socket.send(b"Recherche d'un adversaire...\n")
        # Ici tu peux décider de lancer une partie après l'inscription

    except Exception as e:
        print(f"Erreur de connexion: {e}")
    finally:
        client_socket.close()

# Fonction pour démarrer le serveur
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))  # Écoute sur localhost et port 5555
    server.listen(5)
    print("Le serveur est prêt à accepter les connexions...")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
