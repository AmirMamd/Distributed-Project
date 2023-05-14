import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 3000
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:

            self.client.connect(self.addr)
            # print("try of connect")
            # print("self.client.recv(2048)",self.client.recv(2048))
            return pickle.loads(self.client.recv(2048))
        except:
            print("except of connect")
            pass

    def send(self, data):
        try:
            self.client.send((pickle.dumps(data)))
            # print("gena henaaa",data)
            # print("gena henaaa1", pickle.dumps(data))
            # print("self.client.recv(2048)",self.client.recv(2048))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)