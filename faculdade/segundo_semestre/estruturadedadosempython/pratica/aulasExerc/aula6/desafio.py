import random, string, timeit

def gerar_str(tam=8):
    return "".join(random.choices(string.ascii_letters, k=tam))

n = 50_000
chaves = [gerar_str() for _ in range(n)]
valores = list(range(n))
lista = list(zip(chaves, valores))
tabela = dict(zip(chaves, valores)) # zip combina os itens


consulta = random.sample(chaves, 1_000)

def busca_lista():
    for c in consulta:
        next((v for k, v in lista if k == c), None)

def busca_tabela():
    for c in consulta:
        tabela.get(c)

print("Lista:", timeit.timeit(busca_lista, number=1))
print("Dict:", timeit.timeit(busca_tabela, number=1))
