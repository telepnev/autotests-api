import socket

HOST = 'localhost'
PORT = 12345
messages_history = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

print(f'Сервер запущен на {HOST}:{PORT}')

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Пользователь с адресом: {client_address} подключился к серверу')

    data = client_socket.recv(1024).decode()
    print(f'Пользователь с адресом: {client_address} отправил сообщение: {data}')

    messages_history.append(data)

    response = '\n'.join(messages_history)
    client_socket.send(response.encode())

    client_socket.close()

# python -m tcp_server
# lsof -ti :12345 | xargs kill -9
