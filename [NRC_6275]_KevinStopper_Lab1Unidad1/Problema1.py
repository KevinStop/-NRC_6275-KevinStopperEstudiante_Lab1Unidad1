#Establecemos valores constantes
pi = 3.1416

print("Calculo del Diametro, Circunferencia y area de un circulo")
radio = float(input("Ingrese el valor del radio: "))

#Definimos las formulas a usar
diametro = 2*radio
circunferencia = 2*pi*radio
area = pi*(radio**2)

#Imprimimos el resultado de los ejercicios
print("El diametro del circulo es: " + str(diametro))
print("La circunferencia del circulo es: " + str(circunferencia))
print("El area del circulo es: " + str(area))