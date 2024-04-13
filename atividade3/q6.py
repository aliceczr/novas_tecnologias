lugares_vagos = [10, 2, 1, 3, 0] 
sala = [1, 2, 3, 4, 5]

while True:
    print("Salas disponíveis:", sala)
    sala_escolhida = int(input("Em qual sala você deseja ocupar lugares (ou digite 0 para sair)? "))
    if sala_escolhida == 0:
        print("Programa encerrado.")
        break
    if sala_escolhida not in sala:
        print("Sala inválida. Por favor, escolha uma sala disponível.")
    else:
        indice_sala = sala.index(sala_escolhida)
        saida = int(input(f"Quantos lugares você deseja ocupar na Sala {sala[indice_sala]}? "))
        if saida <= lugares_vagos[indice_sala]:
            lugares_vagos[indice_sala] -= saida 
            print(f"{saida} lugares foram ocupados na Sala {sala[indice_sala]}")
        else:
            print("Desculpe, não há lugares vagos suficientes nessa sala.")
        if 0 in lugares_vagos:
            break
