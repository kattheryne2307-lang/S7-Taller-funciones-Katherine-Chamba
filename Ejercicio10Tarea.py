#10. Fibonacci recursivo

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