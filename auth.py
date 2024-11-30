def authenticate_client(client_socket):
    # Step 1: Send authentication prompts
    client_socket.send("Please enter your username: ".encode())
    username = client_socket.recv(1024).decode()

    client_socket.send("Please enter your password: ".encode())
    password = client_socket.recv(1024).decode()

    # Step 2: Basic username/password validation (could be more complex in real systems)
    if username == "admin" and password == "password":
        client_socket.send("Authentication Successful".encode())
        return True
    else:
        client_socket.send("Authentication Failed".encode())
        client_socket.close()
        return False
