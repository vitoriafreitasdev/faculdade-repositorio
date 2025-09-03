def linear_seach(seq, alvo):
    for i, v in enumerate(seq):
        if v == alvo:
            return i 
    return -1


def binary_search(seq, alvo):
    ini, fim = 0, len(seq) - 1
    while ini <= fim: 
        meio = (ini + fim) // 2
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
