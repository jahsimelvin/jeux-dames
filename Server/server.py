import socket
import threading
import tkinter as tk

# Configuration du serveur
HOST = 'localhost'
PORT = 5555

# Initialisation de la fenêtre Tkinter
root = tk.Tk()
root.title("Serveur du Jeu de Dames - Attente des Joueurs")
root.geometry("400x200")

# Label pour afficher l'état des connexions
status_label = tk.Label(root, text="Serveur en attente de connexions...", font=("Arial", 12))
status_label.pack(pady=20)

# Création du serveur socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)  # On attend exactement 2 joueurs

players = []  # Liste des joueurs connectés

def update_status(message):
    """Met à jour le texte affiché dans la fenêtre Tkinter."""
    status_label.config(text=message)
    root.update_idletasks()  # Rafraîchir la fenêtre

def handle_player(player_socket):
    """Gère les connexions des joueurs et met à jour l'interface graphique."""
    global players

    players.append(player_socket)
    nb_joueurs = len(players)  # Nombre de joueurs connectés

    if nb_joueurs == 1:
        update_status("Player1 connecté. En attente de Player2...")
    elif nb_joueurs == 2:
        update_status("Les deux joueurs sont connectés. Bonne partie à vous !")

def start_server():
    """Démarre le serveur et accepte les connexions des joueurs."""
    while len(players) < 2:  # On attend seulement deux joueurs
        player_socket, _ = server.accept()
        threading.Thread(target=handle_player, args=(player_socket,)).start()

# Lancement du serveur dans un thread séparé pour ne pas bloquer Tkinter
threading.Thread(target=start_server, daemon=True).start()

# Lancer l'interface graphique
root.mainloop()
