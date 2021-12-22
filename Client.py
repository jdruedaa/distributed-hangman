import socket
from hangmanUtilities import draw_hangman

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

response = ClientSocket.recv(1024).decode('utf-8')
print(response)
while True:
    Input = input('>')
    ClientSocket.send(str.encode(Input))
    response = ClientSocket.recv(1024).decode('utf-8')
    print(response)
    try:
        allowed_errors=response.split("\n")[0]
        allowed_errors=allowed_errors.split("= ")[1]
        print(int(allowed_errors))
        draw_hangman(int(allowed_errors))

    except:
        pass

    if response == 'Connection closed':
        break
ClientSocket.close()
