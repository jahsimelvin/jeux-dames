# game.py
class Game:
    def __init__(self, joueur1_id, joueur2_id):
        self.joueur1_id = joueur1_id
        self.joueur2_id = joueur2_id
        self.moves = []  # Liste des mouvements joués
        self.current_player = joueur1_id  # Le joueur qui commence

    def make_move(self, move):
        """
        Fonction pour effectuer un mouvement.
        Chaque mouvement sera ajouté à la liste des mouvements.
        """
        self.moves.append(move)
        self.switch_turn()

    def switch_turn(self):
        """
        Permet de changer de joueur après chaque mouvement.
        """
        if self.current_player == self.joueur1_id:
            self.current_player = self.joueur2_id
        else:
            self.current_player = self.joueur1_id

    def get_game_status(self):
        """
        Retourne l'état actuel de la partie (en cours ou terminée).
        """
        return "en cours"  # Cela peut être étendu pour déterminer la fin de la partie
