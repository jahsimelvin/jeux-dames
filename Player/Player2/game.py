class Game:
    def __init__(self, server):
        self.server = server
        self.board = None  # Le plateau de jeu sera reçu depuis le serveur
        self.player_color = None

    def play(self):
        while True:
            self.display_game_state()
            move = input("Entrez votre coup: ")
            self.send_move_to_server(move)

    def send_move_to_server(self, move):
        self.server.send(move.encode())

    def display_game_state(self):
        # Afficher l'état actuel du jeu
        print("État du jeu:")
        # On reçoit l'état du jeu depuis le serveur (sous forme de texte ou autre)
        state = self.server.recv(1024).decode('utf-8')
        print(state)
