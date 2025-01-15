import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message or message == '!Q':
                print("Disconnected from server.")
                client_socket.close()
                break
            print(f"Server: {message}")
        except:
            print("Connection closed by the server.")
            client_socket.close()
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5559))

    recv_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    recv_thread.start()

    while True:
        message = input()
        if message == '!Q':
            client_socket.send(message.encode('utf-8'))
            print("Exiting chat...")
            client_socket.close()
            break
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
