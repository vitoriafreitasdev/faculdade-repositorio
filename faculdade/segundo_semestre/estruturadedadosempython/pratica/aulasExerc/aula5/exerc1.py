
# pesquisa linear
def linear_seach(seq, alvo):
    # é o index e v é o valor
    for i, v in enumerate(seq):
        # se o valor for igual o alvo, retornará o index onde o item se encontra
        if v == alvo:
            return i 
    # se não encontrar nada retorna -1
    return -1

def binary_search(seq, alvo):
    # ini recebi 0, fim recebi a largura menos -1
    ini, fim = 0, len(seq) - 1

    while ini <= fim:
        # pega o meio do array
        meio = (ini + fim) // 2
        # se encontrar o item, retorna a posição dele
        if seq[meio] == alvo:
            return meio 

        if seq[meio] < alvo:
            ini = meio + 1
        else:
            fim = meio - 1

    return -1 

lista = [1, 2, 3, 4, 5, 6, 7]

print(linear_seach(lista, 7))
print(binary_search(lista, 3))
