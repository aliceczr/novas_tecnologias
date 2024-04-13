palavra = list('Paralelepipedo'.lower())
palavra_tracos = ['_'] * len(palavra)
chute = 0

while chute < 15:
    print('Palavra:', ' '.join(palavra_tracos))

    letra = input('Digite a letra: ').lower()

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_tracos[i] = letra

        if palavra_tracos == palavra:
            print('Parabéns! Você venceu!')
            break
    else:
        chute += 1
        print(f'Letra incorreta! Você tem {15 - chute} tentativas restantes.')

if chute == 15:
    print(f'Você perdeu! A palavra correta era: {"".join(palavra)}')