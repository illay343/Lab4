import socket

# Настройки сервера
HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Сервер запущен на {HOST}:{PORT}")
    
    while True:
        conn, addr = server_socket.accept()  # Принимаем подключение
        with conn:
            print(f"Подключен клиент: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"Клиент {addr} отключился.")
                    break
                print(f"Получено от {addr}: {data.decode()}")
                conn.sendall(data)  # Отправляем данные обратно клиенту
