import socket

def start_tcp_client(host='127.0.0.1', port=12345):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Send a request (this could be an HTTP/2 request or DNS query format)
    request = "GET / HTTP/2 Request"  # Placeholder request for HTTP/2 or DNS
    client_socket.send(request.encode())

    # Receive the response
    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")

    # Close connection
    client_socket.close()

# Start client
start_tcp_client()
