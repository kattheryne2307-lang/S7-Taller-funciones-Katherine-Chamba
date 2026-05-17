#9. Frecuencia de un dígito

def frecuencia(numero,digito):
    contador=0

    for i in str(numero):
        if i==str(digito):
            contador=contador+1

    return contador

numero=int(input("Ingrese un numero entero: "))
digito=int(input("Ingrese un digito: "))

print("La frecuencia es: ",frecuencia(numero,digito))