
import random
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        indice_pivo = random.randint(0, len(array) - 1)
        pivo = array[indice_pivo]
        restantes = array[:indice_pivo] + array[indice_pivo+1:]  # para criar um array sem o pivo
        menores = [i for i in restantes if i <= pivo]
        maiores = [i for i in restantes if i >= pivo]
       
        return quicksort(menores) + [pivo] + quicksort(maiores)


array = [19, 5, 2, 3, 0, 10, 7]
print(quicksort(array))