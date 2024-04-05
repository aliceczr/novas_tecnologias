def separar_digitos(numero):
    digitos = [int(digito) for digito in str(numero)]
    return " ".join(map(str, digitos))

numero = int(input("Digite um número: "))
print(separar_digitos(numero))