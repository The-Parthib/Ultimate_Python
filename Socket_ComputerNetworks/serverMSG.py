import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'
port = 26525

server_socket.bind((host,port))

server_socket.listen(5)

while True:
    client_socket , addr = server_socket.accept()
    print(f'got connection from : {addr}')

    data = client_socket.recv(1024).decode('utf-8')
    print(f'Received msg : {data}')

    message = 'hola client'
    client_socket.send(message.encode('utf-8'))

    client_socket.close()

