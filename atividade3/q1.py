list = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]

maior = list[0]

for elemento in list:
    if elemento > maior:
        maior = elemento

print(f'O maior elemento da lista é : {maior}')

menor = list[0]

for elemento in list:
    if menor > elemento:
        menor = elemento

print(f'O menor elemento da lista é: {menor}')

elementos_pares = []  

for elemento in list:
    if elemento % 2 == 0:
        elementos_pares.append(elemento)  

print("Elementos pares da lista:", elementos_pares)

n1_elemento = 12
count = 0

for elemento in list:
    if elemento == n1_elemento:
        count += 1

print(f'O número de ocorrências do número 12 é de {count} vezes')

somar = 0 

for elemento in list:
    somar += elemento  

media = somar / len(list) 

print(f"A média dos elementos da lista é de {media}")

contador = 0

for elemento in list:
    if elemento < 0 :
        contador += 1

print(f"A soma dos números negativos é de {contador}")

