import socket

# Создаем серверный сокет
HOST = '127.0.0.1'  # Локальный хост
PORT = 65432        # Порт для прослушивания

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Привязываем сокет к хосту и порту
    server_socket.listen()  # Слушаем входящие соединения
    print(f"Сервер запущен на {HOST}:{PORT}")
    
    conn, addr = server_socket.accept()  # Принимаем подключение
    with conn:
        print(f"Подключен клиент: {addr}")
        while True:
            data = conn.recv(1024)  # Получаем данные от клиента
            if not data:
                break  # Если данных нет, завершаем соединение
            print(f"Получено: {data.decode()}")
            conn.sendall(data)  # Отправляем данные обратно клиенту
