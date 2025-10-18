import random
import timeit
import heapq

# Algoritmo de Dijkstra para encontrar caminhos mínimos em grafos sem pesos negativos
def dijkstra(grafo, origem):
    # Inicializa todas as distâncias como infinito
    dist = {v: float('inf') for v in grafo}
    # Distância da origem para ela mesma é 0
    dist[origem] = 0
    # Fila de prioridade (heap) com (distância, vértice)
    fila = [(0, origem)]
    
    while fila:
        # Remove o vértice com menor distância da fila
        d, u = heapq.heappop(fila)
        # Se encontramos um caminho melhor anteriormente, ignora
        if d > dist[u]:
            continue
        # Para cada vizinho do vértice atual
        for v, w in grafo[u]:  
            # Calcula nova distância
            novo = d + w 
            # Se encontrou caminho melhor, atualiza
            if novo < dist[v]:
                dist[v] = novo 
                heapq.heappush(fila, (novo, v))
    return dist 

# Algoritmo de Bellman-Ford para caminhos mínimos (funciona com pesos negativos)
def bellman_ford(grafo, origem):
    # Coleta todos os vértices do grafo
    vertices = set(grafo.keys())
    for arestas in grafo.values():
        for destino, _ in arestas:
            vertices.add(destino)
    
    # Inicializa distâncias e antecessores
    dist = {v: float('inf') for v in vertices}
    antecessor = {}
    dist[origem] = 0

    # Relaxamento das arestas |V|-1 vezes
    for _ in range(len(vertices) - 1):
        for u in vertices:
            for v, peso in grafo.get(u, []):
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    antecessor[v] = u

    # Verifica se há ciclos de peso negativo
    for u in vertices:
        for v, peso in grafo.get(u, []):
            if dist[u] + peso < dist[v]:
                raise ValueError("Ciclo de peso negativo detectado")

    return dist, antecessor

# Geração de grafo aleatório para teste
num_vertices = 200
num_arestas = 400
vertices = [i for i in range(num_vertices)]

# Cria grafo vazio
grafo = {v: [] for v in vertices}

# Adiciona arestas aleatórias
for _ in range(num_arestas):
    u = random.choice(vertices)
    v = random.choice(vertices)
    if u != v:
        peso = random.randint(1, 20)  
        grafo[u].append((v, peso))
    
# Testa os algoritmos de caminho mínimo
origem = int(input("Origem: "))

# Mede tempo de execução
tm_dij = timeit.timeit(lambda: dijkstra(grafo, origem), number=1)
tm_bf = timeit.timeit(lambda: bellman_ford(grafo, origem), number=1)

print(f"Dijkstra: {tm_dij:.4f}s")
print(f"Bellman-Ford: {tm_bf:.4f}s")

## Comparação de algoritmos para Árvore Geradora Mínima

# Cria novo grafo não-direcionado para MST
vertices = 200
arestas = 400
vertice = [i for i in range(vertices)]

# Estruturas para Kruskal e Prim
aresta = []
grafo_adj = {v: [] for v in vertice}

# Gera arestas bidirecionais
for _ in range(arestas):
    u, v = random.sample(vertice, 2)
    peso = random.randint(1, 20)
    aresta.append((peso, u, v))
    grafo_adj[u].append((v, peso))
    grafo_adj[v].append((u, peso)) 

# Algoritmo de Kruskal para MST (usa Union-Find)

# Estruturas para Union-Find
parent = {}
rank = {}

# Find com compressão de caminho
def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

# Union por rank
def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root == v_root:
        return False  # Já estão no mesmo conjunto
    # Une pela altura (rank)
    if rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
    else:
        parent[v_root] = u_root
        if rank[u_root] == rank[v_root]:
            rank[u_root] += 1
    return True

def kruskal(vertice, aresta):
    # Inicializa estruturas Union-Find
    for v in vertice:
        parent[v] = v
        rank[v] = 0
    mst = []  # Árvore geradora mínima
    total = 0  # Peso total
    
    # Ordena arestas por peso e processa da menor para maior
    for peso, u, v in sorted(aresta):
        if union(u, v):  # Se não forma ciclo
            mst.append((u, v, peso))
            total += peso
    return mst, total

# Algoritmo de Prim para MST (usa abordagem gulosa com heap)
def prim(vertice, grafo_adj, inicio):
    visitado = set([inicio])  # Vértices já na MST
    heap = []  # Heap de arestas candidatas
    
    # Adiciona arestas do vértice inicial
    for v, peso in grafo_adj[inicio]:
        heapq.heappush(heap, (peso, inicio, v))
    
    mst = []
    total = 0

    # Expande a MST até incluir todos os vértices
    while heap and len(visitado) < len(vertice):
        peso, u, v = heapq.heappop(heap)
        if v not in visitado:
            visitado.add(v)
            mst.append((u, v, peso))
            total += peso
            # Adiciona novas arestas candidatas
            for to, w in grafo_adj[v]:
                if to not in visitado:
                    heapq.heappush(heap, (w, v, to))
    return mst, total

# Comparação de desempenho entre Kruskal e Prim
inicio_kruskal = timeit.default_timer()
mst_kruskal, total_kruskal = kruskal(vertice, aresta)
tempo_kruskal = timeit.default_timer() - inicio_kruskal

inicio_prim = timeit.default_timer()
mst_prim, total_prim = prim(vertice, grafo_adj, vertice[0])
tempo_prim = timeit.default_timer() - inicio_prim

print(f"Kruskal: peso total = {total_kruskal}, tempo = {tempo_kruskal:.6f}s")
print(f"Prim:    peso total = {total_prim}, tempo = {tempo_prim:.6f}s")