#7. Suma de dígitos mediante función

def suma_digitos(numero):
    suma=0

    while numero>0:
        suma=suma+numero%10
        numero=numero//10

    return suma

numero=int(input("Ingrese un numero: "))

while numero!=0:
    print("La suma es: ",suma_digitos(numero))
    numero=int(input("Ingrese un numero: "))