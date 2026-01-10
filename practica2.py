# crear un programa que permita realizar las operaciones basicas +,-,*,/, utilizando una funcion para cada operacion 
# y un meni principal para desplegar y elegir que operacion realizaremos

op= ""

print(input("""Escoje la operacion a realizar
        1. suma
        2. resta
        3. multiplicacion
        4. division
      
        """))

# funcion que herede los valores y realizar una suma
def suma():
    num1 = print(input("Ingresa el primer numero"))
    num2 = print(input("Ingresa el segundo numero"))
    sum = num1 + num2
    print("la suma de {1} mas {2} es: {0}".format(sum, num1, num2))

def resta():
    num1 = print(input("Ingresa el primer numero"))
    num2 = print(input("Ingresa el segundo numero"))
    rest = num1 - num2
    print("la resta de {1} mas {2} es: {0}".format(sum, num1, num2))

def multiplicacion():
    num1 = print(input("Ingresa el primer numero"))
    num2 = print(input("Ingresa el segundo numero"))
    mult = num1 + num2
    print("la multiplicacion de {1} mas {2} es: {0}".format(mult, num1, num2))

def  divicion():
    num1 = print(input("Ingresa el primer numero"))
    num2 = print(input("Ingresa el segundo numero"))
    div = num1 + num2
    print("la divición de {1} mas {2} es: {0}".format(sum, num1, num2))