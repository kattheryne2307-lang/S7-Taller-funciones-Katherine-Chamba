#19. Contar pares descendentes

def pares(numero):

    if numero<0:
        return

    if numero%2==0:
        print(numero)

    pares(numero-1)

numero=int(input("Ingrese un numero: "))

pares(numero)