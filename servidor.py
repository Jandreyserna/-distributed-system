import socket

##creo un objeto lalmado "my.socket"
my_socket = socket.socket()

#estableco la coneccion con el servidor
#este metodo recibe una tupla el host y el puerto
my_socket.bind(('localhost', 8000))

# Establesco la cantidad de peticiones que puede ejecutar el socket en cola
my_socket.listen(5)
#CREO UN CICLO INFINITO PARA RECIBIR LAS PETICIONES
while True:
    #esta linea retorna dos valores "la conexion" y "la direccion"
    conexion,addr = my_socket.accept()
    print ("Nueva conexion establecida!")
    print (addr)
    #RECIVO LO QUE EL CLIENTE ENVIA
    peticion = conexion.recv(1024)
    print (peticion)

    conexion.send("hola te saludo desde el servidor!".encode())
    conexion.close()
