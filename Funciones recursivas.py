#1. Calcular la serie de Fibonacci

def fibonacci(n):

    if n<0:
        return "No se puede calcular"

    elif n==0:
        return 0

    elif n==1:
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)

numero=int(input("Ingrese la posicion: "))

print("Fibonacci es: ",fibonacci(numero))




#2. Calcular el factorial recursivo

def factorial(n):

    if n<0:
        return "No se puede calcular"

    elif n==0 or n==1:
        return 1

    else:
        resultado=n*factorial(n-1)
        return resultado

numero=int(input("Ingrese un numero: "))

print("El factorial es: ",factorial(numero))