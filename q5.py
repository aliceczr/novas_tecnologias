def separar_digitos(numero):
    digitos = [digito for digito in str(numero) if digito.isdigit()]
    return " ".join(digitos)

numero = input("Digite um número: ")
print(separar_digitos(numero))
