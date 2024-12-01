import socket

# DHCP Message Types
DHCP_DISCOVER = 1
DHCP_OFFER = 2
DHCP_REQUEST = 3
DHCP_ACK = 5
DHCP_NAK = 6

def handle_dhcp_message(message, client_address, server_socket):
    print(f"Received DHCP message: {message}")
    
    # Handle different DHCP message types
    if message == "DHCP_DISCOVER":
        print("Sending DHCP Offer...")
        send_dhcp_offer(client_address, server_socket)
    elif message == "DHCP_REQUEST":
        print("Sending DHCP Ack...")
        send_dhcp_ack(client_address, server_socket)
    else:
        print("Sending DHCP NAK... Invalid message type.")
        send_dhcp_nak(client_address, server_socket)

def send_dhcp_offer(client_address, server_socket):
    response = "DHCP Offer"
    server_socket.sendto(response.encode(), client_address)
    print("DHCP Offer sent.")

def send_dhcp_ack(client_address, server_socket):
    response = "DHCP Ack"
    server_socket.sendto(response.encode(), client_address)
    print("DHCP Ack sent.")

def send_dhcp_nak(client_address, server_socket):
    response = "DHCP NAK"
    server_socket.sendto(response.encode(), client_address)
    print("DHCP NAK sent.")

def start_dhcp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('127.0.0.1', 12345))
    print("DHCP server listening on 127.0.0.1:12345")

    while True:
        message, client_address = server_socket.recvfrom(1024)
        message = message.decode()
        print(f"Received message: {message}")
        
        if message.startswith("DHCP"):
            handle_dhcp_message(message, client_address, server_socket)
        else:
            print(f"Invalid DHCP request from {client_address}, sending NAK...")
            send_dhcp_nak(client_address, server_socket)

if __name__ == "__main__":
    start_dhcp_server()
