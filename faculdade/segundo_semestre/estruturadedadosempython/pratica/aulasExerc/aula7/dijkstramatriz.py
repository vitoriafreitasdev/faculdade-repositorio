import heapq 

def dijkstra_matriz(matriz, origem, vertices):
    n = len(vertices)
    dist = [float('inf')] * n
    origem_idx = vertices.index(origem)
    dist[origem_idx] = 0
    fila = [(0, origem_idx)]
    
    while fila:
        d, u = heapq.heappop(fila)
        if d > dist[u]:
            continue
        for v in range(n):
            w = matriz[u][v]
            if w != 0:  # existe aresta
                novo = d + w
                if novo < dist[v]:
                    dist[v] = novo
                    heapq.heappush(fila, (novo, v))
    
    # converter de volta para nomes dos vértices
    return {vertices[i]: dist[i] for i in range(n)}



vertices = ["A", "B", "C"]
n = len(vertices)

matriz = [[0] * n for _ in range(n)]

def adicionar_arestas_matriz(u, v, peso):
    i, j = vertices.index(u), vertices.index(v)
    matriz[i][j] = peso
    matriz[j][i] = peso 
adicionar_arestas_matriz("A", "B", 5)
adicionar_arestas_matriz("B", "C", 2)

print("Matriz de Adjacência (com pesos): ")
for linha in matriz: 
    print(linha)

# Mostrar vértices
print("\nVértices:")
for v in vertices:
    print(v)

# Mostrar arestas
print("\nArestas (com pesos):")
for i in range(n):
    for j in range(i+1, n):  # usa i+1 pra não repetir arestas no não direcionado
        if matriz[i][j] != 0:
            print(f"{vertices[i]} -- {vertices[j]} (peso {matriz[i][j]})")


print(dijkstra_matriz(matriz, "A", vertices))