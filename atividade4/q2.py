lista1 = [1, 2, 3, 4, 5, 6, 6, 3]
lista2 = [1, 2, 4, 5, 7, 8, 9, 9, 10, 10]

list1 = set(lista1)
list2 = set(lista2)

print(list1.intersection(list2))
print(list1-list2)
print(list2-list1)

n_repetidos = list(list1.union(list2))

print(n_repetidos)

n_lista2 = list(list1.difference(list1))