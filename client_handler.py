import socket
import time
from auth import authenticate_client

# Global variable for active connections
active_connections = 0

def handle_client(client_socket, addr):
    global active_connections
    try:
        # Step 1: Authenticate the client (optional, based on your requirements)
        if not authenticate_client(client_socket):
            return

        # Step 2: Handle the client's request (for now, just echoing back)
        request = client_socket.recv(1024).decode()
        print(f"Received request from {addr}: {request}")
        
        # Simple echo response
        client_socket.send(f"Server Response: Hello {addr}".encode())
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        client_socket.close()
        active_connections -= 1  # Decrease active connection count

