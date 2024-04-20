
def comparar_listas(lista_inicial, lista_modificada):
    elementos_mantidos = set(lista_inicial) & set(lista_modificada)
    novos_elementos = set(lista_modificada) - set(lista_inicial)
    elementos_removidos = set(lista_inicial) - set(lista_modificada)
    
    print("Elementos que não mudaram:", elementos_mantidos)
    print("Novos elementos:", novos_elementos)
    print("Elementos removidos:", elementos_removidos)


lista_inicial = [1, 2, 3, 4, 5]
lista_modificada = [2, 3, 5, 6, 7]
comparar_listas(lista_inicial, lista_modificada)
