# Ejercicio 1: Comparación de Números
# Escribe un programa que pida al usuario un número y 
# determine si es positivo, negativo o cero.

# Ejercicio 2: Clasificación de Edad
# Escribe un programa que pida al usuario su edad y clasifique 
# en una de las siguientes categorías: niño (0-12), adolescente (13-19),
#  adulto (20-64) o adulto mayor (65+).

# Ejercicio 3: Calculadora Simple
# Escribe un programa que actúe como una calculadora simple. 
# Debe pedir al usuario dos números y una operación (+, -, *, /) y
#  luego mostrar el resultado de la operación.

num1 = float(input())
num2 = float(input())
operacion = input()
if operacion == "+":
    print(num1 + num2)
elif operacion == "-":
    print(num1 - num2)
elif operacion == "*":
    print(num1 * num2)
elif operacion == "/":
    if num2 == 0:
        print("El dividendo no puede ser cero..")
    else:
        print(num1 / num2)
