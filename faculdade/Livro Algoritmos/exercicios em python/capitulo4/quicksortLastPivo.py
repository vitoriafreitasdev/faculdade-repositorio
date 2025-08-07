
def quicksort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos -1) #elementos menores que o pivo
        quicksort(arr, partition_pos + 1, right) #elementos maiores que o pivo

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:       
            j -= 1
        if i < j:     
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i


arr = [22, 11, 88, 66, 55, 77, 33, 44]

quicksort(arr, 0, len(arr) - 1)
print(arr)


# versão com pivo aleatorio

import random

def quicksortRandom(arr, left, right):
    if left < right:
        # Escolhe um pivô aleatório e move para a posição 'right'
        random_pivot_index = random.randint(left, right)
        arr[random_pivot_index], arr[right] = arr[right], arr[random_pivot_index]
        
        partition_pos = partitionRandom(arr, left, right)
        quicksortRandom(arr, left, partition_pos - 1)  # Elementos menores que o pivô
        quicksortRandom(arr, partition_pos + 1, right)  # Elementos maiores que o pivô

def partitionRandom(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]  # Pivô está na posição 'right' (já trocado se for aleatório)

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i  # Retorna a posição final do pivô


# Exemplo de uso:
arr2 = [12, 23, 54, 3, 10, 14, 7, 1]
quicksortRandom(arr2, 0, len(arr2) - 1)
print(arr2)  # Saída: [11, 22, 33, 44, 55, 66, 77, 88]