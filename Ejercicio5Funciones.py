#5. Suma de dígitos hasta ingresar 0

def suma_digitos(numero):
    suma=0

    while numero>0:
        suma=suma+numero%10
        numero=numero//10

    return suma

numero=int(input("Ingrese un numero: "))

while numero!=0:
    print("La suma de digitos es: ",suma_digitos(numero))
    numero=int(input("Ingrese un numero: "))