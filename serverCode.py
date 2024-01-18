import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received message: {data.decode('utf-8')}")
        response = input("Enter your response: ")
        client_socket.send(response.encode('utf-8'))
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("paso 1")
    server.bind(('0.0.0.0', 5555))    
    #172.31.8.104
    server.listen(5)
    print("[*] Server listening on port 5555")

    while True:
        
        print("paso 2")
        client, addr = server.accept()
        print("paso 3")
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client,))
        
        print("paso 4")
        client_handler.start()




if __name__ == "__main__":
    start_server()
