import socket


SIZE = 1024
PORT = 12345

my_socket = socket.socket()
my_socket.bind(("", PORT))
my_socket.listen()

print("Welcome to FTP server")

while True:
    client_socket, address = my_socket.accept()
    print(f'{address} is connected')
    
    command = client_socket.recv(SIZE).decode()
    file_name = client_socket.recv(SIZE).decode().split('/')[-1]
    
    if command == 'upload':
        with open(f'mefathim4/socket/server/{file_name}', 'ab+') as f:
            data = client_socket.recv(SIZE)
            
            f.write(data)                

    elif command == 'download':
        with open(file_name, 'rb') as f:
            data = f.read(SIZE)

            while data:
                client_socket.send(data)
                data = f.read(SIZE)

    elif command == 'list':
        pass

    else:
        pass
