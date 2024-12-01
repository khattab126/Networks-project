import socket

def start_tcp_server(host='127.0.0.1', port=12345):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Can handle 5 clients at once

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive the request
        request = client_socket.recv(1024).decode()
        print(f"Received request: {request}")

        # Send a basic response (can be expanded for HTTP/2 or DNS)
        response = "HTTP/2 Server Response"  # Placeholder for HTTP/2 or DNS response
        client_socket.send(response.encode())

        # Close connection
        client_socket.close()

# Start server
start_tcp_server()
