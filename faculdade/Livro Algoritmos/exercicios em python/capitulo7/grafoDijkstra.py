infinto = float("inf")                 # Define uma constante para "infinito" (um número muito grande).

grafo = {}                             # Dicionário que representará o grafo (lista de adjacência).
grafo["inicio"] = {}                   # Cria o nó "inicio" com seus vizinhos ainda vazios.

grafo["inicio"]["a"] = 6               # Aresta de "inicio" para "a" com custo 6.
grafo["inicio"]["b"] = 2               # Aresta de "inicio" para "b" com custo 2.

grafo["a"] = {}                        # Cria o nó "a".
grafo["a"]["fim"] = 1                  # Aresta de "a" para "fim" com custo 1.

grafo["b"] = {}                        # Cria o nó "b".
grafo["b"]["a"] = 3                    # Aresta de "b" para "a" com custo 3.
grafo["b"]["fim"] = 5                  # Aresta de "b" para "fim" com custo 5.

grafo["fim"] = {}                      # Nó "fim" não tem vizinhos (dicionário vazio).


custos = {}                            # Tabela de custos a partir de "inicio" até cada nó conhecido.
custos["a"] = 6                        # Custo inicial conhecido para chegar em "a" (direto do "inicio").
custos["b"] = 2                        # Custo inicial para "b".
custos["fim"] = infinto                # Custo inicial para "fim" é infinito (ainda não conhecido diretamente).

pais = {}                              # Tabela de pais (para reconstruir o caminho de menor custo).
pais["a"] = "inicio"                   # Até aqui, o melhor caminho para "a" vem de "inicio".
pais["b"] = "inicio"                   # O melhor caminho para "b" vem de "inicio".
pais["fim"] = None                     # Ainda não sabemos quem é o pai de "fim".

processados = []                       # Lista de nós cujo menor custo já foi finalizado.

def ache_no_custo_mais_baixo(custos):  # Função que encontra, entre os não processados, o nó com menor custo.
    custo_mais_baixo = float("inf")    # Começa assumindo infinito como menor custo.
    nodo_custo_mais_baixo = None       # E nenhum nó selecionado ainda.
    for nodo in custos:                # Percorre todos os nós que têm custo registrado.
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo   # Atualiza o menor custo encontrado.
            nodo_custo_mais_baixo = nodo  # E guarda qual nó tem esse custo.
    return nodo_custo_mais_baixo       # Retorna o nó com menor custo ainda não processado.

nodo = ache_no_custo_mais_baixo(custos) # Pega o primeiro nó com menor custo (deve ser "b", custo 2).
print(nodo)                             # Imprime esse nó inicial escolhido.

while nodo is not None:                 # Enquanto existir nó a processar...
    custo = custos[nodo]                # Custo atual para chegar neste nó.
    vizinhos = grafo[nodo]              # Dicionário dos vizinhos desse nó com seus custos.
    print(custo)                        # Mostra o custo atual (debug).
    print(vizinhos)                     # Mostra os vizinhos (debug).
    print(vizinhos.keys())              # Mostra apenas as chaves (nomes dos vizinhos).

    for n in vizinhos.keys():           # Para cada vizinho n do nó atual...
        novo_custo = custo + vizinhos[n]# Custo para chegar em n passando pelo nó atual.
        if custos[n] > novo_custo:      # Se esse caminho é melhor (menor) que o conhecido...
            custos[n] = novo_custo      # Atualiza o custo do vizinho.
            pais[n] = nodo              # E diz que o melhor pai de n agora é o nó atual.
    processados.append(nodo)            # Marca o nó atual como processado (finalizado).
    nodo = ache_no_custo_mais_baixo(custos) # Escolhe o próximo nó não processado com menor custo.
    print(f"nodo: {nodo}, custo: {custo}, processados: {processados},")  # Debug do passo.


