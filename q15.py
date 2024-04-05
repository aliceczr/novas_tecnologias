def quadrado_com_soma_impares(n):
    soma = 0
    inicio = 1
    for i in range(n):
        soma += inicio
        inicio += 2
    return soma

numero = int(input("Digite um número inteiro positivo: "))
print("O quadrado de", numero, "usando a soma de ímpares é:", quadrado_com_soma_impares(numero))
