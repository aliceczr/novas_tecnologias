dicionario = {}

soma = 0

palavra =input((f'O que você deseja acrescentar no dicionário ?:'))
i = 0
for letra in palavra:
    if letra.isalpha():
        letra = letra.lower()

        if letra in dicionario:
            dicionario[letra] +=1
        
        else:
            dicionario[letra] = 1

print(dicionario)
