import math

def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

num = int(input("Ingrese un número: "))
print(f"El factorial de {num} es {factorial_iterativo(num)}")

def modulo(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a % b

def raiz_cuadrada(a):
    if a < 0:
        return "No se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(a)

# Validación de entrada
while True:
    try:
        num = float(input("Ingrese un número: "))
        print("Resultado:", raiz_cuadrada(num))
        break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Error: Ingrese un número válido.")