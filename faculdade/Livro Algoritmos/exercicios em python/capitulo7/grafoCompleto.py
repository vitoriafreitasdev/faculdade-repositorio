# Constante para infinito
infinito = float("inf")

# Grafo representado como dicionário de dicionários
grafo = {}
grafo["inicio"] = {"a": 6, "b": 2}
grafo["a"] = {"fim": 1}
grafo["b"] = {"a": 3, "fim": 5}
grafo["fim"] = {}

# Custos iniciais (quanto custa chegar em cada nó a partir de "inicio")
custos = {"a": 6, "b": 2, "fim": infinito}

# Pais iniciais (quem leva ao nó pelo menor caminho conhecido até agora)
pais = {"a": "inicio", "b": "inicio", "fim": None}

# Lista de nós processados
processados = []

# Função que encontra o nó não processado de menor custo
def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo


# ---------- Algoritmo de Dijkstra ----------
nodo = ache_no_custo_mais_baixo(custos)
while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:   # Achou caminho melhor
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)


# ---------- Reconstrução do caminho ótimo ----------
caminho = []
n = "fim"
while n is not None:
    caminho.append(n)
    n = pais[n]
caminho.reverse()

# Resultado final
print("Menor caminho:", caminho)
print("Custo:", custos["fim"])
