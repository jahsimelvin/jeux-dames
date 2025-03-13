# jeux-dames 
DOSSIER SERVER

server.py : Ce fichier contient le serveur principal qui gère les connexions des utilisateurs via sockets, les inscriptions et les connexions en interagissant avec la base de données, ainsi que la mise en place des parties de jeu entre les joueurs. Il crée des threads pour chaque utilisateur connecté afin de gérer les interactions de manière parallèle.

models.py : Ce fichier contient les fonctions permettant d'interagir avec la base de données, notamment pour la création d'utilisateurs, la récupération d'un utilisateur par email, et la gestion de l'historique des parties et des scores. Il permet de maintenir la persistance des données des utilisateurs et des jeux.

config.py : Ce fichier gère la configuration du serveur, notamment les informations sensibles comme les paramètres de connexion à la base de données (hôte, nom d'utilisateur, mot de passe, etc.), et les paramètres de sécurité comme les clés de chiffrement.

database.py : Ce fichier contient les fonctions qui gèrent la connexion à la base de données, ainsi que les opérations liées à la gestion des utilisateurs et de l'historique des parties. Il est utilisé par models.py pour effectuer des requêtes SQL telles que l'ajout de nouveaux utilisateurs et la récupération des informations des utilisateurs.

game.py : Ce fichier contient la logique du jeu de dames, y compris la gestion du plateau de jeu, des mouvements des pions, des règles du jeu (captures, promotion en dame), et de la détermination des gagnants. Il est utilisé par le serveur pour gérer l'état du jeu entre les joueurs.

DOSSIER PLAYER