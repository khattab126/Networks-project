import socket

def start_udp_server(host='127.0.0.1', port=12345):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print(f"UDP Server listening on {host}:{port}")

    while True:
        # Receive message
        message, client_address = server_socket.recvfrom(1024)
        print(f"Received message: {message.decode()} from {client_address}")

        # Send a basic response
        response = "DHCP Server Response"  # Placeholder response for DHCP
        server_socket.sendto(response.encode(), client_address)

# Start UDP server
start_udp_server()
