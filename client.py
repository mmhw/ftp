import socket
import sys

SIZE = 1024
PORT = 12345
my_socket = socket.socket()


def connect_to_server():
    commend = input("[+] to connect press 'connect' and the IP address\n>>> ")

    if len(commend.split(' ')) > 1 and commend.split(' ')[0] == 'connect':
        connect = commend.split(' ')[0]
        server_ip = commend.split(' ')[1]
        
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
        comm = commend.split(' ')[0] 
        file_path = commend.split(' ')[1]
            
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
    
    with open(file_path, 'rb') as f:
        data = f.read(SIZE)
        
        while data:
            my_socket.send(data)
            data = f.read(SIZE)
    
    my_socket.close()
    print("[!] successful\n")

    connect_to_server()


def download(file_name):  
    my_socket.send(b'download')
    my_socket.send(file_name.encode())

    with open(f'/home/david/mefathim4/socket/client/{file_name}', 'wb') as f:
        data = my_socket.recv(SIZE)

        f.write(data)

    print('[!] successful\n')
    connect_to_server()
    

def list_files():
    my_socket.send(b'list')
    
    data = my_socket.recv(SIZE).decode()
    print(f'list of the files:\n{data}\n')
    
    connect_to_server()


if __name__=="__main__":
    print("[+] Welcome to FTP Client\n")
    
    connect_to_server()

    cli()
