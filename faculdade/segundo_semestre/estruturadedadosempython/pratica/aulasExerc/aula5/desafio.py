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


n = int(input("Tamanho da lista: "))

lista = [random.randint(0, 100_000) for _ in range(n)]
alvo = int(input("Valor alvo: "))

t_lin = timeit.timeit(lambda: pesquisa_linear(lista, alvo), number=1)
ordenada = sorted(lista)
t_bin = timeit.timeit(lambda: pesquisa_binaria(lista, alvo), number=1)

print(f"Busca linear: {t_lin:.6f}s")
print(f"Busca binária: {t_bin:.6f}s")



