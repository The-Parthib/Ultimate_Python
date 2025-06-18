import socket;

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

host = 'localhost'
port = 26525

client_socket.connect((host,port));

message = 'hello server';
client_socket.send(message.encode('utf-8'));

data = client_socket.recv(1024).decode('utf-8')
print(f'received from server:{data}')

client_socket.close()