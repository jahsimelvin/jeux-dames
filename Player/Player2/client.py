import socket
import hashlib
from game import Game
from ui import display_game_state

def connect_to_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('localhost', 5555))  # Connexion au serveur

    # Connexion ou inscription de l'utilisateur
    email = input("Email: ")
    mot_de_passe = input("Mot de passe: ")

    # Envoi des informations de connexion
    server.send(email.encode())
    server.send(mot_de_passe.encode())

    # Attendre confirmation de la connexion
    response = server.recv(1024).decode('utf-8')
    print(response)

    if "Connexion réussie!" in response:
        # Lancer le jeu
        game = Game(server)
        game.play()
    else:
        print("Erreur de connexion!")
        server.close()

if __name__ == "__main__":
    connect_to_server()
