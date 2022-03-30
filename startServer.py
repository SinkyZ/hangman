from src.game import Server
from src.gameUtil import *

server = Server()

# Prima data primeste start sau stop trimits de client
mesaj = server.conn_socket.recv(512).decode()

if mesaj != 'START':
    print('Jocul s-a oprit.')
    exit(0)

# genereaza un cuvant random din lista de cuvinte
cuvantTinta = generateRandomWord('hangwords.txt')
cuvantCurent = cuvantToHangman(cuvantTinta)
hangman = []

# completeaza cuvantul cu prima si ultima litera in caz ca apare de mai multe ori
cuvantCurent = completareCuvant(cuvantTinta, cuvantCurent, cuvantTinta[0])
cuvantCurent = completareCuvant(cuvantTinta, cuvantCurent, cuvantTinta[len(cuvantTinta) - 1])

while True:
    server.conn_socket.send((str(cuvantCurent) + "|" + str(hangman)).encode())

    litera = server.conn_socket.recv(512).decode()

    if litera in cuvantTinta:
        cuvantCurent = completareCuvant(cuvantTinta, cuvantCurent, litera)

        won = hasWon(hangman, cuvantCurent)
        if won == 1:
            server.conn_socket.send('CASTIGAT'.encode())
            break
        elif won == 0:
            server.conn_socket.send('PIERDUT'.encode())
            break
    else:
        hangman = completareHangman(hangman)

        won = hasWon(hangman, cuvantCurent)
        if won == 1:
            server.conn_socket.send('CASTIGAT'.encode())
            break
        elif won == 0:
            server.conn_socket.send('PIERDUT'.encode())
            break
