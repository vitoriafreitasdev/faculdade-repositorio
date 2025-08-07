import random

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        indice_pivo = random.randint(0, len(array) - 1)
        pivo = array[indice_pivo]
        restaste = array[:indice_pivo] + array[indice_pivo+1:]
        menores = [i for i in restaste if i <= pivo]
        maiores = [i for i in restaste if i >= pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)
    

array = [19, 5, 2, 3, 0, 10, 7]
print(quicksort(array))

