import socket


HOST = '127.0.0.1'
PORT = 50007

while True:
    email = input('Enter email to send message: ')
    msg = input('Enter message to send: ')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall((email + ' ' + msg).encode('ascii'))
        response = s.recv(1024).decode('ascii')
    if response == 'OK':
        print("Success!")
        exit()
    else:
        print("Something goes wrong: %s\nPlease, enter again." % response)