import socket
import os
from _thread import *
from hangmanUtilities import *
word="Andrew"
correct_guesses=[]
allowed_errors= 4  # "circle,body,hands,legs"


ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
playerCount = 0
currentTurn = 1
turnsPast = 1
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to Hangman, would you like to join an active game? y/n'))

    while True:
        data = connection.recv(2048)
        message = data.decode('utf-8')
        if message == 'y':
            # Connect to room, assign turn and send it to player
            global playerCount
            playerCount += 1
            playerTurn = playerCount
            global currentTurn
            # Later on we might change this for threadcount
            reply = "You're connected to a room and you turn is " + str(playerCount) + ". " \
                "\n Current turn: " + str(currentTurn) + " \n To exit type 'exit'"
            # Add the rules (i.e: send a letter when its your turn or send exit at any time to quit)
            # Add game state
            connection.sendall(str.encode(reply))
            while True:
                # This hard coded limit will be removed later
                global turnsPast
                if turnsPast >= 35:
                    connection.send(str.encode('End reached'))
                    break
                data = connection.recv(2048)
                message = data.decode('utf-8')
                if not data:
                    break
                elif message == 'exit':
                    connection.send(str.encode('Connection closed'))
                    if playerTurn == currentTurn:
                        # TODO reassign playerTurns. Ask the server?
                        # This only works if its the last player
                        if currentTurn >= playerCount:
                            currentTurn = 1
                        else:
                            currentTurn += 1
                    playerCount -= 1
                    break
                elif playerTurn == currentTurn:
                    if len(message) == 1:
                        # Maybe add in elif "and" for checking its a letter in the alphabet
                        # Process letter and reply based on whether its the player's turn and if its correct or not
                        # Send resulting game state
                        global allowed_errors

                        allowed_errors = process_letter(message, word, correct_guesses, allowed_errors)
                        if allowed_errors == 0:
                            draw_hangman(allowed_errors)
                            reply="GAME OVER"

                        else:
                            reply="allowed errors = "+str(allowed_errors)+"\n"+"word = " + str(print_solved(word, correct_guesses))

                    elif message != '':
                        # Process word and reply based on whether its the player's turn and if its correct or not
                        # Send resulting game state
                        # Process word
                        allowed_errors = process_word(message, word, correct_guesses, allowed_errors)
                        if allowed_errors == 0:
                            draw_hangman(allowed_errors)
                            reply="GAME OVER"

                        else:
                            reply="allowed errors = "+str(allowed_errors)+"\n"+"word = " + str(print_solved(word, correct_guesses))


                    if currentTurn >= playerCount:
                        currentTurn = 1
                    else:
                        currentTurn += 1
                    turnsPast += 1
                else:
                    reply = 'Its not your turn yet.'
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
    print('Clients connected: ' + str(ThreadCount))
ServerSocket.close()