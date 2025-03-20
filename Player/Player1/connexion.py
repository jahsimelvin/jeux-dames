import socket
import hashlib
from tkinter import messagebox

def connexion(client_socket, entry_email, entry_password, root):
    email = entry_email.get()
    mot_de_passe = entry_password.get()
    mot_de_passe_hash = hashlib.sha256(mot_de_passe.encode()).hexdigest()

    client_socket.send(f"LOGIN:{email}:{mot_de_passe_hash}".encode('utf-8'))
    reponse = client_socket.recv(1024).decode('utf-8')

    if "SUCCES" in reponse:
        messagebox.showinfo("Connexion réussie", "Vous êtes connecté !")
        root.destroy()  # Fermer la fenêtre après connexion réussie
    else:
        messagebox.showerror("Erreur", "Email ou mot de passe incorrect.")
