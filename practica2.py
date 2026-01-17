# crear un programa que permita realizar las operaciones basicas +,-,*,/, utilizando una funcion para cada operacion 
# y un meni principal para desplegar y elegir que operacion realizaremos

def suma():
    num1 = int(input("Ingresa el primer numero"))
    num2 = int(input("Ingresa el segundo numero"))
    suma = num1 + num2
    print(f"la suma de {num1} mas {num2} es: {suma}")

def resta():
    num1 = int(input("Ingresa el primer numero"))
    num2 = int(input("Ingresa el segundo numero"))
    rest = num1 - num2
    print(f"la resta de {num1} mas {num2} es: {rest}")

def multiplicacion():
    num1 = int(input("Ingresa el primer numero"))
    num2 = int(input("Ingresa el segundo numero"))
    mult = num1 * num2
    print(f"la multiplicacion de {num1} mas {num2} es: {mult}")

def  divicion():
    num1 = int(input("Ingresa el primer numero"))
    num2 = int(input("Ingresa el segundo numero"))
    div = num1 / num2
    print(f"la división de {num1} mas {num2} es: {div}")


op = 0
while op != 5:
    op = int(input("""Escoje la operacion a realizar
        1. suma
        2. resta
        3. multiplicacion
        4. division
        5.salir
        """))
    if op == 1 :
        suma()
    elif op == 2 :
        resta()
    elif op == 3 :
        multiplicacion()
    elif op == 4 :
        divicion()
    elif op == 5 :
        print("saliendo")
        break
    else:
        print("Opcion invalida")