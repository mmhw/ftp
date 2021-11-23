import socket
import os

SIZE = 1024
PORT = 12345

my_socket = socket.socket()
my_socket.bind(("", PORT))
my_socket.listen()
print("[+] Welcome to FTP server\n")


def cli():
    command = client_socket.recv(SIZE).decode()
    
    if command == 'upload':
        upload()

    elif command == 'download':
        download()

    elif command == 'list':
        list_files()
    
    else:
        pass


def upload():
    file_name = client_socket.recv(SIZE).decode().split('/')[-1]
    print(f"[+] [received] upload, file name: {file_name}")

    with open(f'/home/david/mefathim4/socket/server/{file_name}', 'wb+') as f:
        data = client_socket.recv(SIZE)

        while data:
            f.write(data)
            data = client_socket.recv(SIZE)
    
    print("[!] Done")


def download():
    file_name = client_socket.recv(SIZE).decode().split('/')[-1]
    print(f"[+] [received] download, file name: {file_name}")

    with open(f'/home/david/mefathim4/socket/server/{file_name}', 'rb') as f:
        data = f.read(SIZE)

        client_socket.send(data)                          
    
    print("[!] Done")


def list_files():
    print(f"[+] [received] list all files")
    
    all_files = os.listdir('/home/david/mefathim4/socket/server/')        
    
    client_socket.send(str(all_files).encode())

    print("[!] Done")


if __name__=="__main__":
    while True:
        client_socket, address = my_socket.accept()               
        print(f'[!] {address} is connected')
        
        cli()
