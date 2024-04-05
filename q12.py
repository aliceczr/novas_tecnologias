def num_primo_otimizado(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def primeiros_n_primos(n):
    primos = []
    numero = 2
    while len(primos) < n:
        if num_primo_otimizado(numero):
            primos.append(numero)
        numero += 1
    return primos

n = int(input("Digite um número inteiro positivo: "))
print("Os primeiros", n, "números primos são:", primeiros_n_primos(n))
