import socket
from _thread import *
from logic_handler import LogicHandler
import pickle
import random


class Server:
    def __init__(self):
        self.server = "127.0.0.1"
        self.port = 5555

        self.create_server()
        self.create_gamedata()
        self.listen_thread()

    def create_server(self):
        """Création d'un socket accueillant 2 connexions et
        création de 2 instances de controlleurs spécifique à chaque joueur."""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.s.bind((self.server, self.port))
        except socket.error as e:
            str(e)

        # Nombre de connexions attendues
        self.s.listen(2)
        print("En attente de connexions, serveur démarré.")

    def create_gamedata(self):
        self.players = [LogicHandler("x"), LogicHandler("o")]
        self.current_player = random.choice(["x", "o"])
        self.players[0].current_player = self.current_player
        self.players[1].current_player = self.current_player

    def threaded_client(self, conn, player):
        """Cette méthode traite toutes les données du thread. Elle décide de ce qu'il faut faire avec
        les données reçues et quelles données envoyer."""

        # A la première connexion, la méthode va envoyer le controlleur(initié par le serveur) au bon client.
        conn.send(pickle.dumps(self.players[player]))
        reply = ""

        # Une fois la connexion établie, le client peut envoyer différents paquets au serveur.
        # Ici, des classes vides "ResetBoard" et "AskBoard" sont utilisés pour identifier la commande du client.
        while True:
            try:
                # On reçoit ici un objet quelconque.
                data = pickle.loads(conn.recv(2048 * 300))

                # Si il n'y a pas d'objet, c'est que la connexion a été fermée.
                if not data:
                    print("Disconnected")
                    break

                # Demande de remise à zéro du jeu. On ré-initialise les valeurs par défaut.
                elif data.__class__.__name__ == "ResetBoard":
                    self.create_gamedata()
                    print(self.players[0].matrix)

                # Le client demande constament son controlleur stocké sur le serveur.
                elif data.__class__.__name__ == "AskBoard":
                    if player == 1:
                        reply = self.players[1]
                    elif player == 0:
                        reply = self.players[0]

                    #print("Mise à jour du board...")
                    #print("- Reçu: ", data.matrix)
                    #print("- Envoyé: ", reply.matrix)
                    conn.sendall(pickle.dumps(reply))

                else:
                    """Si le client a placé un coup, le controlleur du client est envoyé au serveur qui met à jour
                       le controlleur correspondant du côté serveur et réplique la modification sur le controlleur 
                       de l'autre client.
                       
                       L'autre client pourra voir la modification en demandant son propre controlleur avec 'AskBoard'."""
                    if player == 0:
                        self.players[0] = data
                        self.players[1].matrix = self.players[0].matrix
                        self.players[1].winner_status = self.players[0].winner_status
                        self.players[1].current_player = self.players[0].current_player
                        self.players[1].play_nb = self.players[0].play_nb

                        reply = self.players[0]
                    elif player == 1:
                        self.players[1] = data
                        self.players[0].matrix = self.players[1].matrix
                        self.players[0].winner_status = self.players[1].winner_status
                        self.players[0].current_player = self.players[1].current_player
                        self.players[0].play_nb = self.players[1].play_nb

                        reply = self.players[1]

                    print("- Envoyé: ", data)
                    print("- Reçu : ", reply)

                conn.sendall(pickle.dumps(reply))
            except:
                break

        print("Connexion perdue.")
        self.player_number -= 1
        conn.close()

    def listen_thread(self):
        """Cette boucle écoute et accepte les connexions au serveur et créer un thread entre le serveur et le client."""
        self.player_number = 0
        while True:
            conn, addr = self.s.accept()
            print("Connecté à:", addr)

            start_new_thread(self.threaded_client, (conn, self.player_number))
            self.player_number += 1


srv = Server()





