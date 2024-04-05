
def num_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número: "))
if num_primo(numero):
    print("É um número primo.")
else:
    print("Não é um número primo.")
