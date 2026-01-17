"""
operacion de multiplicacion de a x b utilizando sumas
a=3
b=4
salida: 3+3+3+3=12

"""

# numero por el que se hara la opercion
a= int(input("Valor a: "))
# numero por el que se "multiplica la opercaion"
b= int(input("Valor b: "))
result= 0

if b == 1:
    result = a
    print(f"valor {a} = {result}")
elif b == 2:
    result = a + a
    print(f"Valor {a}+{a} = {result}")
elif b == 3:
    result = a +a +a
    print(f"Valor {a}+{a}+{a} = {result}")
elif b == 4:
    result = a +a +a +a
    print(f"Valor {a}+{a}+{a}+{a} = {result}")
else:
    print("wl valor b tiene que ser entre 1 y 4")
