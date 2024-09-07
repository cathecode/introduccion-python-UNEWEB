#-----------------Proyecto de calculadora-----------------

#Se importa el  módulo que proporciona acceso a las funciones matemáticas.   

import math 

#Se imprimen las opciones disponibles de esta calculdora y algunas instrucciones.

print("----------Calculadora dinámica en Python----------\n")
print("Opciones disponibles:")
print("1. Suma.")
print("2. Resta.")
print("3. Multiplicación.")
print("4. División.")
print("5. Porcentaje.")
print("6. Potencia.")
print("7. Raíz cuadrada.")
print("8. Salir.\n")
print("NOTA: Opción 6 Potencia, el primer número al introducir representa la base y el segundo número es el exponente.")
print("En el caso de la opción 5 porcentaje, devuelve el (%) de la multiplicación de dos números.\n")

#Funciones para cada operación matemática.

#Devuelve la suma de a y b. 
def sumar(a, b):
    return a + b

#Devuelve la resta de a y b.
def restar(a, b):
    return a - b

#Devuelve la multiplicación de a y b.
def multiplicar(a, b):
    return a * b

#Devuelve la división de a y b. En caso contrario devuelve un mensaje.
def dividir(a, b):
    if b != 0:
      return a / b
    else:
        return "Error: No se puede dividir entre cero."  
     
#Devuelve el cálculo del porcentaje de a y b.
def porcentaje(a, b):
    return (a * b) / 100  

#Devuelve el cálculo de la potencia de a y b.
def potencia(a, b):
    return a ** b

#Devuelve la raíz cuadrada de x. En caso contrario devuelve un mensaje.
def raiz_cuadrada(x):
    if x >= 0:
        return math.sqrt(x)
    else: 
      return "Error: No se puede sacar la raíz cuadrada de un número negativo."
    
"""    
Bucle while, se ejecuta hasta que el usuario elija la opción 8 (salir).
Se solicita al usuario que elija una opción entre el 1 al 7, en el caso de la 
opción 7 (raíz cuadrada) se establece una condición aparte, al elejir esta,
el valor introducido por el usuario se almacena en una variable llamada (num)
debido a que solo se requiere un valor para calcular la raíz cuadrada de un número.
En el caso de las demás opciones del 1 al 6, se establece una condición que acepta 
dos valores por el usuario, ya que para sus cálculos matemáticos requieren de dos 
valores, los cuales se almacenan en las variables (num1 y num2). Luego se establecen 
varias condiciones elif, para la instrucción de cada una, llamando a la función
correspondiente de cada operación. 

Se convierten las entradas en float, para que no concatene los valores introducidos
por el usuario, y asi pueda realizar los cálculos correspondientes.

"""  
while True:
     operacion = input("¡Binvenido! Selecciona una opción del 1 al 8: ")
     if operacion == "8":  
        print("Salió del sistema.")  
        break 
     
     if operacion == "7":
         num = float(input("Introduce un número: "))
     
     if operacion in ("1", "2", "3", "4", "5", "6"):
         num1 = float(input("Introduce el 1er número: "))
         num2 = float(input("Introduce el 2do número: "))     

     if operacion == "1":
        print("El resultado de la suma es: ", sumar(num1, num2)) 

     elif operacion == "2":
        print("El resultado de la resta es: ", restar(num1, num2))

     elif operacion == "3":
        print("El resultado de la multiplicación es: ", multiplicar(num1, num2))

     elif operacion == "4":
        print("El resultado de la división es: ", dividir(num1, num2))  
   
     elif operacion == "5":
        print("El resultado del porcentaje es: ", porcentaje(num1, num2))

     elif operacion == "6":
        print("El resultado de la potencia es: ", potencia(num1, num2))

     elif operacion == "7":
        print("El resultado de la raíz cuadrada es: ", raiz_cuadrada(num))    
     
     else:
        print("Opción no válida.")      