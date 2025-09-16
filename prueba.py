def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Ejemplo de uso:
if __name__ == "__main__":
    cantidad = 10  # Cambia este valor para más números
    print(fibonacci(cantidad))