import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 55555

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            # Receive message from server
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # If error occurs, close the connection
            print("An error occurred!")
            client_socket.close()
            break

# Main function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Start a new thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Send messages to the server
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
