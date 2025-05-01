import socket
import threading

host = 'localhost'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

print(f"Server listening on {host}:{port}")

clients = []
numbers = []

def handle_client(conn, addr):
    print(f"Client connected from {addr}")

    data = conn.recv(1024).decode('utf-8')
    print(f"Received from {addr}: {data}")
    
    try:
        num = int(data)
        numbers.append(num)
        clients.append(conn)
    except ValueError:
        conn.send("Invalid number".encode('utf-8'))
        conn.close()
        return

    # Wait until both numbers are received
    while len(numbers) < 2:
        pass  # busy wait (for simplicity; can be optimized with threading.Event)

    result = sum(numbers)
    conn.send(f"Sum = {result}".encode('utf-8'))
    print(f"Sent sum to client : {addr}")
    conn.close()

# Accept exactly 2 clients
for _ in range(2):
    conn, addr = server_socket.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()