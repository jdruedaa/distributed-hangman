import socket

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
    if response == 'Connection closed':
        break
ClientSocket.close()

