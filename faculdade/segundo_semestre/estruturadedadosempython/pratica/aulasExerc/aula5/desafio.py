import random, timeit 

def pesquisa_linear(lista, alvo):
    for i in range(0, len(lista)):
        if lista[i] == alvo:
            return i 
    return -1

def pesquisa_binaria(lista, alvo):
    ini = 0
    fim = len(lista) - 1
    
    while ini <= fim:
        meio = (ini + fim) // 2
        
        if lista[meio] == alvo:
            return meio 
        if lista[meio] < alvo: 
            ini = meio + 1
        else: 
            fim = meio - 1

    return -1 


lista_teste = [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(pesquisa_binaria(lista_teste, 5))

n = int(input("Tamanho da lista: "))

lista = [random.randint(0, 100_000) for _ in range(n)]
alvo = int(input("Valor alvo: "))

t_lin


