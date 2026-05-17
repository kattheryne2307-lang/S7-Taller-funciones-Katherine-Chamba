#2. Factorial de varios numeros

def factorial(numero):

    resultado=1

    for i in range(1,numero+1):
        resultado=resultado*i

    return resultado

contador=0

numero=int(input("Ingrese un numero: "))

while numero!=0:

    print("El factorial es: ",factorial(numero))

    contador=contador+1

    numero=int(input("Ingrese un numero: "))

print("Cantidad total de numeros: ",contador)