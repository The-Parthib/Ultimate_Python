import socket

def calculate_checksum(data: str) -> int:
    return sum(data.encode()) % 256

host = 'localhost'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server listening on {host}:{port}")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    # Receive data and checksum
    received = conn.recv(1024).decode('utf-8')

    if '>>' not in received:
        conn.send("Invalid format!".encode('utf-8'))
        conn.close()
        break

    data, checksum = received.split('>>')
    
    try:
        checksum = int(checksum)
    except ValueError:
        conn.send("Invalid checksum!".encode('utf-8'))
        conn.close()
        break

    calc_checksum = calculate_checksum(data)

    print(f"Received: {data}, Checksum: {checksum}, Calculated: {calc_checksum}")

    if checksum == calc_checksum:
        conn.send("Checksum OK. Data received.".encode('utf-8'))
    else:
        conn.send("Checksum mismatch. Data corrupted.".encode('utf-8'))

    conn.close()
    break  # Stop after handling one client