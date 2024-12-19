import socket

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Сервер запущен на {HOST}:{PORT}")
    
    conn, addr = server_socket.accept()
    with conn:
        print(f"Подключен клиент: {addr}")
        with open('received_file.txt', 'wb') as file:  # Открываем файл для записи
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)  # Записываем данные в файл
        print("Файл успешно сохранен.")
