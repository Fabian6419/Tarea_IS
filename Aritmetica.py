import math

def factorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

num = int(input("Ingrese un número para saber el factorial: "))
print(f"El factorial de {num} es {factorial_iterativo(num)}")

def modulo(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

try:
    a = int(input("Ingrese el primer número para dividir: "))
    b = int(input("Ingrese el segundo númeroque divide: "))
    resultado = modulo(a, b)
    print("El módulo es:", resultado)
except ValueError:
    print("Error: Ingrese solo números enteros.")

def raiz_cuadrada(a):
    if a < 0:
        return "No se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(a)

# Validación de entrada
while True:
    try:
        num = float(input("Ingrese un número para saber la raiz cuadrada: "))
        print("Resultado:", raiz_cuadrada(num))
        break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Error: Ingrese un número válido.")
        
def valor_absoluto(num):
    return abs(num)

num = float(input("Ingresa un número para calcular su valor absoluto: "))
print(f"El valor absoluto de {num} es {valor_absoluto(num)}")


def suma(a, b):
    return a + b

a = float(input("Ingresa el Primer número para la suma: "))
b = float(input("Ingresa el Segundo número para la suma: "))
print(f"La suma de {a} y {b} es {suma(a, b)}")