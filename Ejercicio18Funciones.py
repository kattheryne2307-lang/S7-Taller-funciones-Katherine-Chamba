#18. Contar descendente hasta cero

def descendente(numero):

    if numero<0:
        return

    print(numero)

    descendente(numero-1)

numero=int(input("Ingrese un numero: "))

descendente(numero)