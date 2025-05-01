import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port
host = 'localhost'
port = 26524

# Bind to the port
server_socket.bind((host, port))

# Queue up to 5 requests
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

while True:
    # Establish a connection
    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")

    # Receive data
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from client: {data}")

    # Send a response
    response = "Hello Client!"
    client_socket.send(response.encode('utf-8'))

    client_socket.close()