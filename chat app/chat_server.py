import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 55555

# List to hold connected clients
clients = []

# Function to handle client connections
def handle_client(client):
    while True:
        try:
            # Receive message from client
            message = client.recv(1024).decode('utf-8')
            broadcast(message)
        except:
            # If error occurs, remove the client and close the connection
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break

# Function to broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.send(message.encode('utf-8'))

# Main function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"Server is listening on {HOST}:{PORT}")

    while True:
        # Accept incoming connection
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Add client to the list
        clients.append(client)

        # Start a new thread to handle the client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    start_server()
