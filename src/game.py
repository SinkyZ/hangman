import socket


# Se initializeaza conexiunea cu client-ul in constructorul clasei server
class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('127.0.0.1', 27578))
        self.server_socket.listen(1)
        self.conn_socket, self.client_address = self.server_socket.accept()


# Se initializeaza conexiunea cu server-ul in constructorul clasei client
class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', 27578))
