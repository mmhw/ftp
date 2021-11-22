import socket
import sys

SIZE = 1024
PORT = 12345
my_socket = socket.socket()


def connect_to_server():
    commend = input("[+] to connect press 'connect' and the IP address\n"
                                ">>> ")
    if len(commend.split(' ')) > 1 and commend.split(' ')[0] == 'connect':
        connect, server_ip = commend.split(' ')
        try:
            my_socket.connect((server_ip, PORT))
            print("[+] connection successful")
            return 1
    
        except:
            print("[!] connection unsuccessful")
            sys.exit()
    
    else:
        print("[!] Try again")
        connect_to_server()


def cli():
    commend = input("\n[+] to upload press 'upload' and the file path\n"
                    "[+] to download press 'download' and the file name \n"
                    "[+] to list all files press 'list'\n"
                    ">>> ")
    
    if len(commend.split(' ')) == 1 and commend == 'list':
        list_files()

    elif len(commend.split(' ')) > 1:
        comm , file_path = commend.split(' ')
            
        if comm == 'upload':
            upload(file_path)

        elif comm == 'download':
            download(file_path)

        elif comm == 'list':
            list_files()

        else:
            print("[!] Unknown command")
            cli()

    else:
        print("[!] Unknown command")
        cli()


def upload(file_path):    
    my_socket.send(b'upload')
    my_socket.send(file_path.encode())

    try:
        with open(file_path, 'rb') as f:
            data = f.read(SIZE)
        
            while data:
                my_socket.send(data)
                data = f.read(SIZE)
    
        print("[!] successful")

        cli()

    except:
        print("[!] Bad file path")

        cli()


def download(file_name):  
    my_socket.send(b'download')
    my_socket.send(file_name.encode())

    with open(file_name, 'wb') as f:        
        while True:
            data = my_socket.recv(SIZE)
            
            if not data:
                break

            f.write(data)
    
    print('successful')

    cli()


def list_files():
    my_socket.send(b'list')
    
    while True:
        data = my_socket.recv(SIZE)
        
        if not data:
            break

        print(data)
    
    cli()

    
if __name__=="__main__":
    print("[+] Welcome to FTP Client\n")
    
    connect_to_server()

    cli()
