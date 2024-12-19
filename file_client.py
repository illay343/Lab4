import socket

HOST = '127.0.0.1'
PORT = 65433
FILE_PATH = 'test_file.txt'  # Укажите путь к вашему файлу

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    with open(FILE_PATH, 'rb') as file:  # Открываем файл для чтения
        while chunk := file.read(1024):  # Читаем файл порциями
            client_socket.sendall(chunk)  # Отправляем данные серверу
    print("Файл успешно отправлен серверу.")
