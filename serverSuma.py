import socket

##creo un objeto lalmado "my.socket"
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#estableco la coneccion con el servidor
#este metodo recibe una tupla el host y el puerto
my_socket.bind(('localhost', 8887))

# Establesco la cantidad de peticiones que puede ejecutar el socket en cola
my_socket.listen(5)
#CREO UN CICLO INFINITO PARA RECIBIR LAS PETICIONES
while True:
    #esta linea retorna dos valores "la conexion" y "la direccion"
    conexion,addr = my_socket.accept()
    print ("Nueva conexion establecida!")
    print (addr)
    #RECIVO LO QUE EL CLIENTE ENVIA
    peticion = conexion.recv(1024).decode()
    print (peticion)
    resultado = peticion[1] + peticion[2]
    resultado = str(resultado)
    conexion.send(resultado.encode())
    conexion.close()
