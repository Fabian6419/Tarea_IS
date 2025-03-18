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
