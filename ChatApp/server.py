import socket
import threading

def handle_client(client_socket, addr):
    print(f"Client {addr} connected.")

    def receive_messages():
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message or message == '!Q':
                    print(f"Client {addr} has left the chat.")
                    client_socket.close()
                    break
                print(f"Client {addr}: {message}")
            except:
                print(f"Client {addr} connection error.")
                client_socket.close()
                break

    recv_thread = threading.Thread(target=receive_messages)
    recv_thread.start()

    while True:
        try:
            response = input("Server: ")
            client_socket.send(response.encode('utf-8'))
        except:
            print(f"Client {addr} connection error.")
            client_socket.close()
            break

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5559))
    server.listen(5)
    print("Server started, waiting for connections...")

    try:
        while True:
            client_socket, addr = server.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_thread.start()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()
