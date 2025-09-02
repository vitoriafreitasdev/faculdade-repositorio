
import time 
from collections import deque
import time 
from typing import List

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



def quick_sort(arr: List[int], inicio=0, fim=None):
    if fim is None:
        fim = len(arr) - 1
    while inicio < fim:
        if fim - inicio < 32:  
            insertion(arr, inicio, fim)
            return
        pivo = mediana_tres(arr, inicio, fim)
        i, j = inicio, fim
        while i <= j:
            while arr[i] < pivo:
                i += 1
            while arr[j] > pivo:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i + 1, j - 1

        if j - inicio < fim - i:
            quick_sort(arr, inicio, j)
            inicio = i
        else:
            quick_sort(arr, i, fim)
            fim = j

def mediana_tres(a: List[int], i: int, j: int) -> int:
    k = (i + j) // 2
    if a[i] > a[k]:
        a[i], a[k] = a[k], a[i]
    if a[k] > a[j]:
        a[k], a[j] = a[j], a[k]
    if a[i] > a[k]:
        a[i], a[k] = a[k], a[i]
    return a[k]

def insertion(a: List[int], i: int, j: int):
    for x in range(i + 1, j + 1):
        chave, y = a[x], x - 1
        while y >= i and a[y] > chave:
            a[y + 1] = a[y]
            y -= 1
        a[y + 1] = chave



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
quick_res = quick_sort(lst)
print(quick_res)
t1 = time.time()
quick_time = t1 - t0 

print(f"Buble Sort tempo: {bubble_time}")

print(f"Merge Sort tempo: {merge_time}")

print(f"Quik Sort tempo: {quick_time}")
