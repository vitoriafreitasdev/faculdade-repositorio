import random
import time 
from collections import deque
import time 

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 -i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista 


def merge_sort(esquerda, direita):
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
  
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

lista = [3, 5, 1, 9, 7, 10, 6, 8, 53]
tam = 20000

lst = list(range(tam))

n = len(lst)
meio = n // 2
metade = lst[meio-1]
direita = lst[:metade]
esquerda = lst[metade:]

direita_ordenada = sorted(direita)  
esquerda_ordenada = sorted(esquerda)  


    
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




t0 = time.time() 
bubble_res = bubble_sort(lst)
print(bubble_res)
t1 = time.time()
bubble_time = t1 - t0 

t0 = time.time() 
merge_res = merge_sort(direita_ordenada, esquerda_ordenada)
print(merge_res)
t1 = time.time()
merge_time = t1 - t0 

t0 = time.time() 
quick_res = quicksortRandom(lst, 0, len(lst) - 1)
print(quick_res)
t1 = time.time()
quick_time = t1 - t0 

print(f"Buble Sort tempo: {bubble_time}")

print(f"Merge Sort tempo: {merge_time}")

print(f"Quik Sort tempo: {quick_time}")
