import socket
import hashlib
from tkinter import messagebox

def inscription(client_socket, entry_email, entry_password):
    email = entry_email.get()
    mot_de_passe = entry_password.get()
    mot_de_passe_hash = hashlib.sha256(mot_de_passe.encode()).hexdigest()

    client_socket.send(f"SIGNUP:{email}:{mot_de_passe_hash}".encode('utf-8'))
    reponse = client_socket.recv(1024).decode('utf-8')

    if "INSCRIPTION_REUSSIE" in reponse:
        messagebox.showinfo("Inscription réussie", "Vous êtes inscrit, connectez-vous !")
    else:
        messagebox.showerror("Erreur", "Cet email est déjà utilisé.")
