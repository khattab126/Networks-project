import socket
import threading
import sys
import os
sys.path.append(os.getcwd())
from client_handler import handle_client
from cli import display_server_status

# Global variable to track active connections
active_connections = 0
server_running = True  # Flag to control the server loop

# Define a lock to synchronize the stopping process
stop_lock = threading.Lock()

def start_server(host, port):
    global active_connections, server_running
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
    server.bind((host, port))  # Bind server to IP and port
    server.listen(5)  # Max backlog of 5 clients
    print(f"Server started on {host}:{port}")

    while server_running:
        try:
            client_socket, addr = server.accept()  # Wait for client connections
            print(f"Accepted connection from {addr}")
            active_connections += 1  # Increment active connection counter
            # Handle each client in a new thread
            client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_handler.start()
        except Exception as e:
            print(f"Error in server loop: {e}")

    server.close()  # Close server socket when the server is stopped
    print("Server has been stopped.")

def run_server():
    host = '127.0.0.1'
    port = 4433  # Port number
    start_server(host, port)

def stop_server():
    global server_running
    with stop_lock:  # Ensure only one thread modifies the flag at a time
        server_running = False  # Stop the server loop
    print("Stopping the server...")

if __name__ == "__main__":
    # Start the server in a new thread
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    # Start the CLI monitoring in the main thread
    display_server_status()

    # Optionally add a command to stop the server (e.g., 'exit' command)
    while True:
        command = input("Enter 'exit' to stop the server: ")
        if command.lower() == 'exit':
            stop_server()  # Stop the server when 'exit' is typed
            break

    # Wait for the server thread to finish before exiting the program
    server_thread.join()  # Ensure the server thread has stopped before exiting
    print("Server stopped successfully.")


print(f"Current working directory: {os.getcwd()}")
