def fibonacci(n):
    if n <= 0:
        return "N/A"
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

n = int(input("Digite um número inteiro maior ou igual a 3: "))
print("O", n, "º termo da série de Fibonacci é:", fibonacci(n))
