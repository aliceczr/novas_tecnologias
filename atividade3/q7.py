grid = [['00','01','02'], ['10', '11','12'], ['20', '21', '22']]

for i, linha in enumerate(grid):
    for j, coluna in enumerate(grid):
        print(grid[i][j], end=' ')
    print("")

venceu = False
velha = False
tentativas = 0

while not venceu and not velha:

    jogada = input('Escolha X ou O:')
    linha = int(input("Em qual linha: "))
    coluna = int(input("Em qual coluna: "))

    grid[linha][coluna] = jogada

    tentativas +=1

    for i, linha in enumerate(grid):
        for j, coluna in enumerate(grid):
            print(grid[i][j], end=' ')
        print("")
    
    if (grid[0][0]==grid[1][1]==grid[2][2]):
        venceu = True

    if (grid[0][2]==grid[1][1]==grid[2][0]):
        venceu = True
        
    for i in range(0, len(grid)):
        if (grid[i][0]==grid[i][1]==grid[i][2]):
            venceu = True
        
    for i in range(0, len(grid)):
        if (grid[0][i]==grid[1][i]==grid[2][i]):
            venceu = True
            break


if venceu is True:
    print('Você Venceu !!!')
else:
    print('Deu Velha !!!')
        
            
    
    


