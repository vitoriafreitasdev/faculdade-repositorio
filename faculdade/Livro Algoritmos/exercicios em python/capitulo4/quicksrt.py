def quicksort(array):
    last = len(array) - 1
    if len(array) < 2:
        return array
    else:
        pivo = array[last]
        menores = [i for i in array[:-1] if i <= pivo]
        maiores = [i for i in array[:-1] if i >= pivo]
        #menores = [i for i in array[1:] if i <= pivo] para ultilizar o primeiro elemento como pivo
        #maiores = [i for i in array[1:] if i >= pivo]
        
        return quicksort(menores) + [pivo] + quicksort(maiores)


array = [19, 5, 2, 3, 0, 10, 7]
print(quicksort(array))