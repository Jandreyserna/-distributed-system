import socketserver
import socket

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.cadena = self.request.recv(1024).decode()
                print("Cliente:", self.cadena)
                print("Cliente:", self.cadena[0])
                print("Cliente:", self.cadena[1])
                print("Cliente:", self.cadena[2])
                self.resultado = self.cadena[1] + self.cadena[2]
                print(self.resultado)
                if self.cadena[0] == 1:
                    self.resultado = self.cadena[1] + self.cadena[2]
                    print("Cliente:", self.cadena)
                    self.cadenasendserver = input("servidor: ")
                    self.request.send(self.resultado.encode())
        except Exception as exc:
            print("Error ", exc)

    def Suma(cadena):
        host= "localhost"
        port= 8887
        socket1=socket.socket()
        socket1.connect((host,port))
        try:
            socket1.send(cadena.encode())
            resultado = socket1.recv(1024).decode()
        except Exception as exc:
            print("Error" , exc)
        socket1.close()
        return resultado

host= "localhost"
port = 8888
server1= socketserver.TCPServer((host,port),MyTcpHandler)

print ("Servidor Corriendo")
server1.serve_forever()
