from src.game import Client
from src.gameUtil import *

client = Client()

mesaj = input('Tastati START pentru a incepe jocul: ')
client.client_socket.send(mesaj.encode())

if mesaj != 'START':
    print("Jocul s-a oprit.")
    exit(0)

while True:
    mesaj = client.client_socket.recv(512).decode()

    if mesaj == 'CASTIGAT':
        print('Felicitari, ati castigat!')
        break
    elif mesaj == 'PIERDUT':
        print('Ati pierdut...')
        break

    mesajSplit = strListFormat(mesaj)
    print(mesajSplit)

    mesaj = input('Introduceti o litera: ')
    client.client_socket.send(mesaj.encode())
