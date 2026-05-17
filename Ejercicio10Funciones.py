#10. Factorial de un número

def factorial(numero):
    resultado=1

    for i in range(1,numero+1):
        resultado=resultado*i

    return resultado

numero=int(input("Ingrese un numero: "))

print("El factorial es: ",factorial(numero))