import socket

host = 'localhost'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

number = input("Enter a number to send to the server: ")
client_socket.send(number.encode('utf-8'))

result = client_socket.recv(1024).decode('utf-8')
print(f"Server response: {result}")

client_socket.close()