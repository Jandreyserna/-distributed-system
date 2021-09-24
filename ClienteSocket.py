import socket
from os import system
import json


host= "localhost"
port= 8888
socket1=socket.socket()
socket1.connect((host,port))

try:
    while True:
        # cadena = input("Cliente: ")
        # socket1.send(cadena.encode(encoding='utf_8', errors= 'strict').strip())


        op = 7
        while op != 0:
            print("\n")
            print(".....BIENVENIDO AL MENU DE OPERACIONES.......")
            print("#1. Hacer una suma.")
            print("#2. Hacer una resta")
            print("#3. Hacer una multiplicaciòn")
            print("#4. Hacer una Divisiòn")
            print("#5. Hacer una potenciaciòn")
            print("#6. Hacer una logaritmaciòn")
            print("#0. Salir.")
            op = int(input('Elija una opcion por favor: '))

            if op == 1:
                op = op
                num1 = int(input('digite el primer numero a sumar: '))
                num2 = int(input('digite el segundo numero a sumar: '))
                lista = [op,num1,num2]
                lista = json.dumps(lista)
                socket1.send(lista.encode())
                cadenarecservidor = socket1.recv(1024).decode('utf_8')
                print("servidor", cadenarecservidor)
            if op == 2:
                resta = "resta"
                socket1.send(resta.encode('utf_8'))
                cadenarecservidor = socket1.recv(1024).decode('utf_8')
                print("servidor", cadenarecservidor)
            if op == 3:
                multi = "multiplicaciòn"
                socket1.send(multi.encode('utf_8'))
                cadenarecservidor = socket1.recv(1024).decode('utf_8')
                print("servidor", cadenarecservidor)
            if op == 4:
                Divi = "Divisiòn"
                socket1.send(Divi.encode('utf_8'))
                cadenarecservidor = socket1.recv(1024).decode('utf_8')
                print("servidor", cadenarecservidor)
            if op == 5:
                pote = "potenciaciòn"
                socket1.send(pote.encode('utf_8'))
                cadenarecservidor = socket1.recv(1024).decode('utf_8')
                print("servidor", cadenarecservidor)
            if op == 6:
                log = "logaritmaciòn"
                socket1.send(log.encode('utf_8'))
                cadenarecservidor = socket1.recv(1024).decode('utf_8')
                print("servidor", cadenarecservidor)
            if op == 0:
                system("cls")
                socket1.close()
                print("Gracias ¡Hasta luego!")

            system("cls")


except Exception as exc:
    print("Error" , exc)

socket1.close()
