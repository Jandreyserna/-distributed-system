import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('localhost', 8000))

my_socket.send("hola desde el cliente!".encode())
respuesta = my_socket.recv(1024)
print(respuesta)
print("\n")
print(".....BIENVENIDO AL MENU DE OPERACIONES.......")
print("#1. Hacer una suma.")
print("#2. Hacer una resta")
print("#3. Hacer una multiplicaciòn")
print("#4. Hacer una Divisiòn")
print("#5. Hacer una potenciaciòn")
print("#6. Hacer una logaritmaciòn")
print("#0. Salir.")
op = 7
while op != 0:
    op = int(input('Elija una opcion por favor: '))

    if op > 0 and op < 7:
        # my_socket.connect(('localhost', 8000))
        my_socket.send("hola hl desde el cliente!".encode())

my_socket.close()

# import socket
#
# HOST = '127.0.0.1'  # The server's hostname or IP address
# PORT = 65432        # The port used by the server
#
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)
#
# print('Received', repr(data))
