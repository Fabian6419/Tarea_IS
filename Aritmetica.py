import math

# Gonzales Acuña Fabian 
def factorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

num = int(input("Ingrese un número: "))
print(f"El factorial de {num} es {factorial(num)}")

# Pinto Salazar Mauricio 
def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

try:
    a = int(input("Ingrese el primer número para dividir: "))
    b = int(input("Ingrese el segundo númeroque divide: "))
    resultado = division(a, b)
    print("El módulo es:", resultado)
except ValueError:
    print("Error: Ingrese solo números enteros.")

# Lopez Juana Jhoselyn 
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

# Zeballos Bladimir         
def valor_absoluto(num):
    return abs(num)

num = float(input("Ingresa un número para calcular su valor absoluto: "))
print(f"El valor absoluto de {num} es {valor_absoluto(num)}")


# Caceres Telleria Jaime Cristhian
def suma(a, b):
    return a + b

a = float(input("Ingresa el Primer número para la suma: "))
b = float(input("Ingresa el Segundo número para la suma: "))
print(f"La suma de {a} y {b} es {suma(a, b)}")

# Quisbert Medrano Jose Armando
def calcular_hipotenusa(c1, c2):
    return math.sqrt(c1**2 + c2**2)

cA = float(input("Ingrese la longitud del primer cateto: "))
cB = float(input("Ingrese la longitud del segundo cateto: "))

hipotenusa = calcular_hipotenusa(cA, cB)
print(f"La hipotenusa del triángulo es: {hipotenusa:.2f}")

# Arroyo Aranibar Gudsalen
def numeros_naturales(n):
    """Genera y muestra los primeros n números naturales."""
    if n < 1:
        print("El número debe ser mayor o igual a 1.")
        return
    
    naturales = list(range(1, n + 1))
    print("Números naturales:", naturales)

# Ejemplo de uso
try:
    n = int(input("Ingrese un número entero positivo: "))
    numeros_naturales(n)
except ValueError:
    print("Por favor, ingrese un número entero válido.")

# Sirpa Escalera Steve Jason    
def resta(a, b):
    return a - b

a = float(input("Ingrese el primer número para restar: "))
b = float(input("Ingrese el segundo número para restar: "))

resultado = resta(a, b)
print("El resultado de la resta es:", resultado)

# Flores Benavides Eddy Alexander 
def calcular_impares(limite):
    return [num for num in range(1, limite + 1) if num % 2 != 0]
limite = int(input("Ingrese un número límite para calcular impares: "))
print(f"Números impares hasta {limite}: {calcular_impares(limite)}")

# Aranibar Mamani Madahi
def calcular_divisores(n):
    return [i for i in range(1, n + 1) if n % i == 0]
n = int(input("Ingrese un número para calcular sus divisores: "))
print(f"Los divisores de {n} son: {calcular_divisores(n)}")

# Calicho Garcia Jhair Brayan
def convertir_a_binario(n):
    if n == 0:
        return "0"  # Caso especial para el 0
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario  # Añadir el residuo al principio
        n = n // 2  # Dividir el número por 2, descartando el residuo
    return binario

# Solicitar un número al usuario
n = int(input("Ingresa un número decimal para convertirlo a binario: "))

# Mostrar el número en binario
print(f"El número {n} en binario es: {convertir_a_binario(n)}")

