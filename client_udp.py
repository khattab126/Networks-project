import socket

def start_udp_client(host='127.0.0.1', port=12345):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send a message (this could be a DHCP Discover message)
    message = "DHCP Discover"  # Placeholder for DHCP message
    client_socket.sendto(message.encode(), (host, port))

    # Receive the response
    response, server_address = client_socket.recvfrom(1024)
    print(f"Received from server: {response.decode()}")

    # Close socket
    client_socket.close()

# Start client
start_udp_client()
