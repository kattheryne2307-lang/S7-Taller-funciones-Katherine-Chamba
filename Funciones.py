#Sin parametro
"""def saludar ():
    nombre=input("Ingrese su nombre: ")
    print("Bienvenido/a",nombre,"a la clase de algoritmos.")

saludar()
"""
#Con parametro
"""def SaludarNombre(nombre):
    print("Hola "+ nombre +" les saluda!.")

SaludarNombre("Katherine Chamba")

#Ingresando el nombre
nombre=input("Ingrese su nombre: ")
SaludarNombre(nombre)
"""
#Con dos parametros
def multiplicar(numero1,numero2):
    multiplicacion=numero1*numero2
    return multiplicacion
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
print(multiplicar(numero1,numero2))