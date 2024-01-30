import socket
import threading
import sys

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received message: {data.decode('utf-8')}")
        except socket.error as e:
            print(f"Error receiving data: {e}")
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)
    print("[*] Server listening on port 5555")

    while True:
        try:
            client, addr = server.accept()
            print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

            client_handler = threading.Thread(target=handle_client, args=(client,))
            client_handler.start()

            # Non-blocking input to check for user input
            threading.Thread(target=check_user_input, args=(client,)).start()

        except KeyboardInterrupt:
            print("Server shutting down.")
            server.close()
            sys.exit()

def check_user_input(client_socket):
    while True:
        try:
            response = input("Enter your response (or type 'exit' to stop): ")
            if response.lower() == 'exit':
                client_socket.close()
                break
            client_socket.send(response.encode('utf-8'))
        except socket.error as e:
            print(f"Error sending data: {e}")
            break

if __name__ == "__main__":
    start_server()
