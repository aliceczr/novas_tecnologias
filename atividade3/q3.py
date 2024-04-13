

expressao = input("Digite a expressão com parênteses: ")


pilha = []


for char in expressao:
    if char == '(':
        pilha.append(char) 
    elif char == ')':
        if not pilha:  
            print("Erro: Os parênteses estão incorretos!")
            break
        else:
            pilha.pop() 


if not pilha:
    print("Os parênteses estão corretos!")
else:
    print("Erro: Os parênteses estão incorretos!")
