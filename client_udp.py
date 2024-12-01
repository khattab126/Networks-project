import socket

def send_dhcp_discover():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto("DHCP_DISCOVER".encode(), ('127.0.0.1', 12345))
    
    response, _ = client_socket.recvfrom(1024)
    print(f"Received from server: {response.decode()}")
    
    # Simulate sending a valid DHCP Request
    client_socket.sendto("DHCP_REQUEST".encode(), ('127.0.0.1', 12345))
    response, _ = client_socket.recvfrom(1024)
    print(f"Received from server: {response.decode()}")
    
    # Simulate sending an invalid DHCP message (which should trigger a DHCP NAK)
    client_socket.sendto("INVALID_DHCP_REQUEST".encode(), ('127.0.0.1', 12345))
    response, _ = client_socket.recvfrom(1024)
    print(f"Received from server: {response.decode()}")
    
    client_socket.close()

if __name__ == "__main__":
    send_dhcp_discover()
