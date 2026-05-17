#8. Area y longitud de circunferencia

import math

def circunferencia(r=1):

    area=math.pi*r*r

    longitud=2*math.pi*r

    return area,longitud

radio=float(input("Ingrese el radio: "))

area,longitud=circunferencia(radio)

print("El area es: ",area)
print("La longitud es: ",longitud)