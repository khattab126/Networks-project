import time
from client_handler import active_connections

def display_server_status():
    while True:
        print(f"Server running... Active connections: {active_connections}")
        time.sleep(5)  # Update every 5 seconds
