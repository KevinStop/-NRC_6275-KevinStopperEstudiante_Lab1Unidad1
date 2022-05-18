print("Ingresar dos números y realizar todas las operaciones aritméticas.")

#Le pedimos al usuario que ingrese los numeros mediante consola
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo nuero: "))

#Operaciones aritmeticas
suma = num1+num2
resta = num1-num2
multiplicacion = num1*num2
division = num1/num2

#Imprimimos el resultado
print("El resultado de la suma es: " + str(suma))
print("El resultado de la resta es: " + str(resta))
print("El resultado de la multiplicacion es: " + str(multiplicacion))
if(num1==0):#Si el numero 1 es 0 la division no es posible
    print("No se puede dividir entre 0")
elif(num2==0):#Si el numero 2 es 0 la division no es posible
    print("No se puede dividir entre 0")
else:
    print("El resultado de la division es: " + str(division))