#4. Fahrenheit a centigrados

def centigrados(f):

    c=5*(f-32)/9

    return c

f=float(input("Ingrese la temperatura en Fahrenheit: "))

print("La temperatura en centigrados es: ",centigrados(f))