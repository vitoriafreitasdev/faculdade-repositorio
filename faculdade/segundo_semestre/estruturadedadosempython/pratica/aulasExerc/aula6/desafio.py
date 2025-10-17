import heapq
import random
import timeit

n = 50_000
# Cria uma lista com 50 mil números aleatórios entre 1 e 1 milhão
dados = [random.randint(1, 1_000_000) for _ in range(n)]

def heap_invertendo_sinal():
    heap = []
    # heappush insere elemento mantendo a propriedade de heap
    # Aqui invertemos o sinal (-v) para simular uma max-heap,
    # pois o heapq por padrão é um min-heap
    for v in dados:
        heapq.heappush(heap, -v)
    # heappop remove o menor elemento (que, com sinal invertido,
    # equivale ao maior valor original)
    while heap:
        heapq.heappop(heap)


class MaxValue:
    __slots__ = ("valor",)  # economiza memória, define atributos fixos
    def __init__(self, valor):
        self.valor = valor

    # Método de comparação especial usado pelo heapq
    # Aqui invertemos o critério: maior valor é considerado "menor"
    # para o heapq, simulando uma max-heap real.
    def __lt__(self, outro):
        return self.valor > outro.valor

    def __repr__(self):
        return f"{self.valor}"

def heap_classe_propria():
    heap = []
    # heappush insere objetos da classe MaxValue
    for v in dados:
        heapq.heappush(heap, MaxValue(v))
    # heappop remove mantendo a ordem definida em __lt__
    while heap:
        heapq.heappop(heap)


# Mede o tempo de execução de cada abordagem apenas 1 vez
tempo_sinal = timeit.timeit(heap_invertendo_sinal, number=1)
tempo_classe = timeit.timeit(heap_classe_propria, number=1)

# Mostra os resultados de forma formatada
print(f"Invertendo sinal: {tempo_sinal:.4f} s")
print(f"Classe própria:   {tempo_classe:.4f} s")
