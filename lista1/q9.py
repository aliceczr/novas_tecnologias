
def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Divisão por zero não é possível"

def multiplicacao(x, y):
    return x * y

opcoes = {
    "1": adicao,
    "2": subtracao,
    "3": divisao,
    "4": multiplicacao
}

while True:
    print("Menu:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Divisão")
    print("4. Multiplicação")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")
    
    if escolha == "5":
        break
    
    if escolha in opcoes:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        resultado = opcoes[escolha](x, y)
        print("Resultado:", resultado)
    else:
        print("Opção inválida")
