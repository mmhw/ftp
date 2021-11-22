import socket
import sys

SIZE = 1024
PORT = 12345
my_socket = socket.socket()


def connect_to_server(server_ip):
    try:
        my_socket.connect((server_ip, PORT))
        print("[+] connection successful")
        return 1
    
    except:
        print("[!] connection unsuccessful")
        sys.exit()


def cli():
    commend = input("\n[+] press 1 to upload file\n"
                      "[+] press 2 to download file\n"
                      "[+] press 3 to list all files\n"
                      "[+] press 4 to exit\n>>> ")
    
    if commend == '1':
        upload()

    if commend == '2':
        download()

    if commend == '3':
        list_files()
    
    if commend == '4':
        exit()


def upload():
    file_path = input("[+] Please enter the file path\n>>> ")
    
    my_socket.send(b'upload')
    my_socket.send(file_path.encode())

    with open(file_path, 'rb') as f:
        data = f.read(SIZE)
        
        while data:
            my_socket.send(data)
            data = f.read(SIZE)
    
    print('successful')
    
    cli()


def download():
    file_name = input("[+] Please enter the file anme\n>>> ")
    
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


def exit():
    print("[!] goodbye!")
    
    my_socket.close()


if __name__=="__main__":
    print("[+] Welcome to FTP Client\n")

    if len(sys.argv) < 2:
        print("Next time please enter IP address")

    else:
        server_ip = sys.argv[1]
        connect_to_server(server_ip)

        cli()
