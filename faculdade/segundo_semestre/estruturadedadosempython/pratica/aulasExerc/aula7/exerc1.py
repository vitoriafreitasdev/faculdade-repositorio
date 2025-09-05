import heapq 

def dijkstra(grafo, origem):
    dist = {v: float('inf') for v in grafo}
    dist[origem] = 0
    fila = [(0, origem)]
    
    while fila:
        d, u = heapq.heappop(fila)
        if d > dist[u]:
            continue
        for v, w in grafo[u]:  # percorre vizinhos de u
            novo = d + w 
            if novo < dist[v]:
                dist[v] = novo 
                heapq.heappush(fila, (novo, v))
    return dist 


# Grafo como dicionário
grafo = {
    "A": [],
    "B": [],
    "C": []
}

def adicionar_aresta_lista(u, v, peso):
    grafo[u].append((v, peso))
    grafo[v].append((u, peso))  # não direcionado

# Adicionando arestas
adicionar_aresta_lista("A", "B", 5)
adicionar_aresta_lista("B", "C", 2)

print("\nLista de Adjacência (com pesos):")
for vertice, vizinhos in grafo.items():
    print(f"{vertice}: {vizinhos}")

print("\nDijkstra a partir de B:")
print(dijkstra(grafo, "B"))
