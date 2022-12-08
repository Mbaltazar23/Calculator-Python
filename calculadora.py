import sys

# variables para la manipulacion de datos (calculos matematicos)
n1 = 0
n2 = 0

# mensaje en consola para ver las opciones
menu = """
   1- Sumar
   2- Restar
   3- Multiplicar
   4- Dividir
   5- Potencia
   6- Raiz
   7- Salir
"""
# metodos para el calculo del algoritmo

def Sumar():
    print("Ingrese el primer numero: ")
    n1 = float(input())
    print("Ingrese el segundo numero: ")
    n2 = float(input())
    print("El resultado es: ", round(n1 + n2))


def Restar():
    print("Ingrese el primer numero : ")
    n1 = float(input())
    print("Ingrese el segundo numero : ")
    n2 = float(input())
    print("El resultado es: ", round(n1 - n2))


def Multiplicar():
    print("Ingrese el primer numero : ")
    n1 = float(input())
    print("Ingrese el segundo numero : ")
    n2 = float(input())
    print("El resultado es: ", round(n1 * n2))


def Dividir():
    print("Ingrese el primer numero : ")
    n1 = float(input())
    print("Ingrese el segundo numero : ")
    n2 = float(input())
    print("El resultado es: ", n1 / n2)


def Potencia():
    print("Ingrese el primer numero : ")
    n1 = float(input())
    print("Ingrese el segundo numero : ")
    n2 = float(input())
    print("El resultado es: ", round(n1 ** n2))


def Raiz():
    print("Ingrese el primer numero : ")
    n1 = float(input())
    print("Ingrese el segundo numero : ")
    n2 = float(input())
    print("El resultado es: ", n1 ** (1 / n2))


# metodo principal donde se ejecutara el programa

print("Bienvenido a la Calculadora")
while True:
    print(menu)
    print("Ingrese una opcion a realizar : ")
    opc = int(input())
    if opc == 1:
        Sumar()
    elif opc == 2:
        Restar()
    elif opc == 3:
        Multiplicar()
    elif opc == 4:
        Dividir()
    elif opc == 5:
        Potencia()
    elif opc == 6:
        Raiz()
    elif opc == 7:
        print("Gracias por probar la calculadora :)")
        sys.exit()
