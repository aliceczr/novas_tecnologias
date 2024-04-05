def operacoes_numericas(a,b):
    soma = a + b
    sub = a - b
    mult = a * b
   

    if b != 0:
        divisao = a / b 
    else:
        divisao = "Divisão por zero não é possível"
    
    return soma, sub, mult, divisao


a = int(input("Digite o primeiro numero inteiro: "))
b = int(input("Digite o segundo numero inteiro"))

result = operacoes_numericas(a,b)

print("Soma:", result[0])
print("Subtração:", result[1])
print("Multiplicação:", result[2])
print("Divisão:", result[3])
