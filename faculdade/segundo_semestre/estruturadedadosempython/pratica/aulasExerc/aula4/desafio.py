import time 
from typing import List
import random

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            #  Verifica se o elemento atual é maior que o próximo
            if lista[j] > lista[j + 1]:
                # TROCA os elementos de lugar
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista  # retorna a lista ordenada


def merge_sort(esquerda, direita):
    resultado = []
    i = j = 0
    
    #Enquanto houver elementos em ambas as listas
    while i < len(esquerda) and j < len(direita):
        # Compara o menor elemento de cada metade
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])  # adiciona o menor
            i += 1
        else:
            resultado.append(direita[j])  # adiciona o menor da direita
            j += 1
  
    # Adiciona os elementos restantes (de uma das metades)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado  #resultado da fusão (merge) ordenada



def quicksort(array):
    if len(array) < 2:
        return array  # caso base (vetor pequeno já está ordenado)
    else:
        #  Escolhe um pivô aleatoriamente
        indice_pivo = random.randint(0, len(array) - 1)
        pivo = array[indice_pivo]

        # Remove o pivô do array
        restantes = array[:indice_pivo] + array[indice_pivo+1:]

        #  Cria lista com valores menores ou iguais ao pivô
        menores = [i for i in restantes if i <= pivo]

        #  Cria lista com valores maiores ou iguais ao pivô
        maiores = [i for i in restantes if i >= pivo]
       
        # Recursão e concatenação final
        return quicksort(menores) + [pivo] + quicksort(maiores)


lista = [3, 5, 1, 9, 7, 10, 6, 8, 53]
tam = 20000
lst = list(range(tam))  # cria uma lista com 20.000 números ordenados
n = len(lst)
meio = n // 2
metade = lst[meio-1]
direita = lst[:metade]
esquerda = lst[metade:]
t0 = time.time() 
direita_ordenada = sorted(direita)  
esquerda_ordenada = sorted(esquerda)  
t1 = time.time()
sorted_time = t1 - t0 


#  BUBBLE SORT
t0 = time.time() 
bubble_res = bubble_sort(lst)
t1 = time.time()
bubble_time = t1 - t0 


#  MERGE SORT
t0 = time.time() 
merge_res = merge_sort(direita_ordenada, esquerda_ordenada)
t1 = time.time()
merge_time = t1 - t0 


# QUICKSORT ALEATÓRIO
t0 = time.time() 
quick_res = quicksort(lst)
t1 = time.time()
quick_time = t1 - t0 


print(f"Bubble Sort tempo: {bubble_time}")
print(f"Merge Sort tempo: {merge_time}")
print(f"Quik Sort pivô aleatório tempo: {quick_time}")
print(f"Tempo de ordenar a direita e esquerda com sorted: {sorted_time}")



# QUICKSORT (mediana de três + insertion)

def quick_sort(arr: List[int], inicio=0, fim=None):
    if fim is None:
        fim = len(arr) - 1
    while inicio < fim:
        #  Caso o intervalo seja pequeno, usa insertion sort (otimização)
        if fim - inicio < 32:
            insertion(arr, inicio, fim)
            return
        
        #  Escolhe o pivô pela mediana de três
        pivo = mediana_tres(arr, inicio, fim)
        i, j = inicio, fim

        #  Particiona o vetor
        while i <= j:
            while arr[i] < pivo:
                i += 1
            while arr[j] > pivo:
                j -= 1
            if i <= j:
                # TROCA de posição dos elementos fora do lugar
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i + 1, j - 1

        #  Escolhe qual metade resolver primeiro (reduz profundidade da recursão)
        if j - inicio < fim - i:
            quick_sort(arr, inicio, j)
            inicio = i
        else:
            quick_sort(arr, i, fim)
            fim = j



def mediana_tres(a: List[int], i: int, j: int) -> int:
    k = (i + j) // 2  # elemento do meio
    # 🔁 Reordena os três para achar a mediana (a[k])
    if a[i] > a[k]:
        a[i], a[k] = a[k], a[i]
    if a[k] > a[j]:
        a[k], a[j] = a[j], a[k]
    if a[i] > a[k]:
        a[i], a[k] = a[k], a[i]
    return a[k]  # retorna o valor da mediana


def insertion(a: List[int], i: int, j: int):
    for x in range(i + 1, j + 1):
        chave, y = a[x], x - 1
        # 🔁 Move elementos maiores que a chave para a direita
        while y >= i and a[y] > chave:
            a[y + 1] = a[y]
            y -= 1
        # ⬅️ Insere a chave na posição correta
        a[y + 1] = chave

# QUICKSORT (MEDIANA DE TRÊS)
t0 = time.time() 
quick_res = quick_sort(lst)
t1 = time.time()
quick_mediana = t1 - t0 
print(f"Quik Sort com mediana tempo: {quick_mediana}")
