import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8080)
sock.bind(server_address)

sock.listen(1)

while True:

    connection, client_address = sock.accept()

    try:

        print('Connection from', client_address[0])

    finally:

        connection.close()