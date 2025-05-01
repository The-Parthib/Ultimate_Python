import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port
host = 'localhost'
port = 26524

# Connection to hostname on the port
client_socket.connect((host, port))

# Send some data
message = "Hello Server!"
client_socket.send(message.encode('utf-8'))

# Receive response
data = client_socket.recv(1024).decode('utf-8')
print(f"Received from server: {data}")

client_socket.close()