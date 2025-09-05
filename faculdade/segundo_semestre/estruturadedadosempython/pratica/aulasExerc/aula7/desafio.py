import random
import timeit
import heapq

def dijkstra(grafo, origem):
    dist = {v: float('inf') for v in grafo}
    dist[origem] = 0
    fila = [(0, origem)]
    
    while fila:
        d, u = heapq.heappop(fila)
        if d > dist[u]:
            continue
        for v, w in grafo[u]:  
            novo = d + w 
            if novo < dist[v]:
                dist[v] = novo 
                heapq.heappush(fila, (novo, v))
    return dist 

def bellman_ford(grafo, origem):
    vertices = set(grafo.keys())
    for arestas in grafo.values():
        for destino, _ in arestas:
            vertices.add(destino)
    
    dist = {v: float('inf') for v in vertices}
    antecessor = {}
    dist[origem] = 0

    for _ in range(len(vertices) - 1):
        for u in vertices:
            for v, peso in grafo.get(u, []):
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    antecessor[v] = u

    for u in vertices:
        for v, peso in grafo.get(u, []):
            if dist[u] + peso < dist[v]:
                raise ValueError("Ciclo de peso negativo detectado")

    return dist, antecessor


num_vertices = 200
num_arestas = 400
vertices = [f"V{i}" for i in range(num_vertices)]

grafo = {v: [] for v in vertices}


for _ in range(num_arestas):
    u = random.choice(vertices)
    v = random.choice(vertices)
    if u != v:
        peso = random.randint(1, 20)  
        grafo[u].append((v, peso))
    
origem = "V0"

tm_dij = timeit.timeit(lambda: dijkstra(grafo, origem), number=1)
tm_bf = timeit.timeit(lambda: bellman_ford(grafo, origem), number=1)

print(f"Dijkstra: {tm_dij:.4f}s")
print(f"Bellman-Ford: {tm_bf:.4f}s")

## Calculando árvore geradora mínima com Kruskal e com Prim:

# criar um grafo aleatório

vertices = 50
arestas = 200
vertice = [f"V{i}" for i in range(vertices)]

aresta = []
grafo_adj = {v: [] for v in vertice}

for _ in range(arestas):
    u, v = random.sample(vertice, 2)
    peso = random.randint(1, 20)
    aresta.append((peso, u, v))
    grafo_adj[u].append((v, peso))
    grafo_adj[v].append((u, peso)) 

# Kruskal 

parent = {}
rank = {}

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    u_root = find(u)
    v_root = find(v)
    if u_root == v_root:
        return False
    if rank[u_root] < rank[v_root]:
        parent[u_root] = v_root
    else:
        parent[v_root] = u_root
        if rank[u_root] == rank[v_root]:
            rank[u_root] += 1
    return True

def kruskal(vertice, aresta):
    for v in vertice:
        parent[v] = v
        rank[v] = 0
    mst = []
    total = 0
    for peso, u, v in sorted(aresta):
        if union(u, v):
            mst.append((u, v, peso))
            total += peso
    return mst, total

# Com Prim 

import heapq

def prim(vertice, grafo_adj, inicio):
    visitado = set([inicio])
    heap = []
    for v, peso in grafo_adj[inicio]:
        heapq.heappush(heap, (peso, inicio, v))
    mst = []
    total = 0

    while heap and len(visitado) < len(vertice):
        peso, u, v = heapq.heappop(heap)
        if v not in visitado:
            visitado.add(v)
            mst.append((u, v, peso))
            total += peso
            for to, w in grafo_adj[v]:
                if to not in visitado:
                    heapq.heappush(heap, (w, v, to))
    return mst, total


# Comparação de pesos e tempos: 

inicio_kruskal = timeit.default_timer()
mst_kruskal, total_kruskal = kruskal(vertice, aresta)
tempo_kruskal = timeit.default_timer() - inicio_kruskal

inicio_prim = timeit.default_timer()
mst_prim, total_prim = prim(vertice, grafo_adj, vertice[0])
tempo_prim = timeit.default_timer() - inicio_prim

print(f"Kruskal: peso total = {total_kruskal}, tempo = {tempo_kruskal:.6f}s")
print(f"Prim:    peso total = {total_prim}, tempo = {tempo_prim:.6f}s")
