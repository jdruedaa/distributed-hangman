import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to Hangman, would you like to join an active game? y/n'))
    while True:
        data = connection.recv(2048)
        message = data.decode('utf-8')
        if message == 'y':
            # Connect to room, assign turn and send it to player
            reply = "You're connected to a room and you turn is TODO. Current turn: TODO \n To exit type 'exit'"
            # Add the rules (i.e: send a letter when its your turn or send exit at any time to quit)
            # Add game state
            connection.sendall(str.encode(reply))
            while True:
                data = connection.recv(2048)
                message = data.decode('utf-8')
                if not data:
                    break
                elif message == 'exit':
                    connection.send(str.encode('Connection closed'))
                    break
                elif len(message) == 1:
                    # Maybe add in elif "and" for checking its a letter in the alphabet
                    # Process letter and reply based on whether its the player's turn and if its correct or not
                    # Send resulting game state
                    reply = 'Letter recieved'
                elif message != '':
                    # Process word and reply based on whether its the player's turn and if its correct or not
                    # Send resulting game state
                    reply = 'Word recieved'
                connection.sendall(str.encode(reply))
            break
        elif message == 'n':
            connection.send(str.encode('Connection closed'))
            break
        else:
            connection.send(str.encode('Unknown answer, please try again'))
    connection.close()

    global ThreadCount
    ThreadCount -= 1
    print('Players connected: ' + str(ThreadCount))


while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,))
    ThreadCount += 1
    print('Players connected: ' + str(ThreadCount))
ServerSocket.close()
