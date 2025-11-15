import socket

HOST = 'localhost'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_socket.send("Я пользователь - 2".encode())

response = client_socket.recv(1024).decode()
print(response)

client_socket.close()


# python -m tcp_client