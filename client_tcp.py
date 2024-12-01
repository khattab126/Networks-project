import socket

def send_http2_request():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))
    client_socket.send("GET / HTTP/1.1".encode())

    # Receive main HTTP/2 response
    response = client_socket.recv(1024).decode()
    print(f"Received from server: {response}")
    
    # Receive pushed data (additional resources)
    pushed_data = client_socket.recv(1024).decode()
    print(f"Received pushed data: {pushed_data}")
    
    client_socket.close()

if __name__ == "__main__":
    send_http2_request()
