import socket
import sys


PORT = 12345

s = socket.socket()


def connect_to_server(server_ip):
    try:
        s.connect((server_ip, PORT))
        print("[+] connection successful")
        return 1
    
    except:
        sys.exit()
        print("[+] connection successful")


def upload():
    pass


def download():
    file_name = input("[+] Please enter the file anme\n>>> ")
    print(file_name)
    s.send(file_name.encode())

    with open(file_name, 'wb') as f:
        
        while True:
            data = s.recv(1024)
            
            if not data:
                break

            f.write(data)


def list_files():
    pass
"""
my_socket.send('menachem'.encode())
data = my_socket.recv(4024).decode()
print(f"The server sent {data}")

my_socket.close()
"""

if __name__ == "__main__":
    print("[+] Welcome to FTP Client\n")

    if len(sys.argv) < 2:
        print("Next time please enter IP address")

    else:
        server_ip = sys.argv[1]
        connect_to_server(server_ip)

        commend = input("\n[+] If you want to upload file press 1\n[+] If you want to download file press 2\n[+] If you want to list all files press 3\n>>> ")

        if commend == '1':
            upload()

        if commend == '2':
            download()

        if commend == '3':
            list_files()

