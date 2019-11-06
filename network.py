import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048 * 300))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048 * 300))
        except socket.error as e:
            print(e)

    def ask_board(self):
        return self.send(AskBoard())

    def reset_board(self):
        return self.send(ResetBoard())


class AskBoard:
    def __init__(self):
        self.ask = "ask"


class ResetBoard:
    def __init__(self):
        self.board = "board"