import socket

# Настройки клиента
HOST = '127.0.0.1'  # Локальный хост
PORT = 65432        # Порт сервера

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))  # Подключаемся к серверу
    message = input("Введите сообщение для отправки: ")
    client_socket.sendall(message.encode())  # Отправляем сообщение
    data = client_socket.recv(1024)  # Получаем ответ от сервера
    print(f"Ответ от сервера: {data.decode()}")
