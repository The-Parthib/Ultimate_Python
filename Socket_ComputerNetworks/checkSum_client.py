import socket

def calculate_checksum(data: str) -> int:
    return sum(data.encode()) % 256

host = 'localhost'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

message = "Parthib Panja"
checksum = calculate_checksum(message)

# Send message + checksum separated by a delimiter
payload = f"{message}>>{checksum}"
client_socket.send(payload.encode('utf-8'))

# Receive server response
response = client_socket.recv(1024).decode('utf-8')
print(f"Server says: {response}")

client_socket.close()