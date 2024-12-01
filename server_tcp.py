import socket
import threading

# HTTP/2 server error frame
def send_http2_error_frame(client_socket, error_code):
    error_frame = f"Error: {error_code}"
    client_socket.send(error_frame.encode())

def handle_http2_request(client_socket, request):
    if not is_valid_http2_frame(request):
        send_http2_error_frame(client_socket, "PROTOCOL_ERROR")
    else:
        # Simulate multiplexing: send the main response and then a server push.
        response = "HTTP/2 Server Response: Main Page"
        client_socket.send(response.encode())
        
        # Simulate server push: additional data sent to the client (before client requests it)
        server_push_data = "HTTP/2 Push Response: Additional Resources"
        client_socket.send(server_push_data.encode())

def is_valid_http2_frame(request):
    # Basic validation: ensure request contains proper HTTP/2 headers
    return request.startswith("GET")

def client_handler(client_socket, client_address):
    request = client_socket.recv(1024).decode()
    print(f"Received request: {request}")
    handle_http2_request(client_socket, request)
    client_socket.close()

def start_http2_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    print("HTTP/2 server listening on 127.0.0.1:12345")
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        threading.Thread(target=client_handler, args=(client_socket, client_address)).start()

if __name__ == "__main__":
    start_http2_server()
