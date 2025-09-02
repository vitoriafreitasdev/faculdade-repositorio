def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 -i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista 

lista = [3, 5, 1, 4, 7, 10]

print(bubble_sort(lista))

    