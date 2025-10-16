import random, timeit
def pesquisa_linear(lista, alvo):

    #Realiza uma busca linear no array. Percorrendo cada elemento até encontrar o alvo, se não achar retorna -1
    
    for i in range(0, len(lista)):      
        if lista[i] == alvo:            
            return i                   
    return -1                           

def pesquisa_binaria(lista, alvo):
    """
    Realiza uma busca binária na lista.
    Requer que a lista esteja ordenada.
    Divide o espaço de busca pela metade a cada iteração.
    """
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


# teste com 250 elementos
n = 250
# Vair gerar uma lista com 250 números entre 0 e 100.000
lista = [random.randint(0, 100_000) for _ in range(n)]
alvo = 30  # Define o número que será procurado

# Mede o tempo da busca linear 
t_lin = timeit.timeit(lambda: pesquisa_linear(lista, alvo), number=1)
# Ordena a lista para a busca binária funcionar corretamente
ordenada = sorted(lista)
# Mede o tempo da busca binária, o number=1 significa que só vai executar uma vez
t_bin = timeit.timeit(lambda: pesquisa_binaria(ordenada, alvo), number=1)

print(f"Busca linear com 250 elementos: {t_lin:.6f}s")
print(f"Busca binária com 250 elementos: {t_bin:.6f}s")

# teste com 500 elementos
n = 500
# Gera uma nova lista com 500 elementos
lista = [random.randint(0, 100_000) for _ in range(n)]
alvo = 30

t_lin = timeit.timeit(lambda: pesquisa_linear(lista, alvo), number=1)
ordenada = sorted(lista)
t_bin = timeit.timeit(lambda: pesquisa_binaria(ordenada, alvo), number=1)

print(f"Busca linear com 500 elementos: {t_lin:.6f}s")
print(f"Busca binária com 500 elementos: {t_bin:.6f}s")

# teste 1000 elementos
n = 1000
# Gera uma nova lista com 1000 elementos
lista = [random.randint(0, 100_000) for _ in range(n)]
alvo = 30

t_lin = timeit.timeit(lambda: pesquisa_linear(lista, alvo), number=1)
ordenada = sorted(lista)
t_bin = timeit.timeit(lambda: pesquisa_binaria(ordenada, alvo), number=1)

print(f"Busca linear com 1000 elementos: {t_lin:.6f}s")
print(f"Busca binária com 1000 elementos: {t_bin:.6f}s")