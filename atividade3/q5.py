V = [9,8,7,12,0,13,21] 

par = []
impar = []
for elementos in V:
    if elementos % 2 == 0:
        par.append(elementos)
    else:
        impar.append(elementos)


print("Elementos pares da lista:", par)
print("Elementos impares da lista:", impar)
