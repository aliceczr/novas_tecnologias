T = [-10, -8, 0, 1, 2, 5, -2,-4]

soma = 0
maior = 0
for elementos in T:
    if elementos > maior:
        maior = elementos

    soma += elementos

media = soma/len(T)

print(f'O maior elemento é {maior} e a temperatura média é {media}')
