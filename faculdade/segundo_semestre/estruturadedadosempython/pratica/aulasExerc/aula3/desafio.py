from collections import deque

def bfs(grafo, origem, destino):
    fila = deque([[origem]])
    visitados = {origem}

    while fila: 
        caminho = fila.popleft()
        atual = caminho[-1]
        
        if atual == destino:
            
            distancia_total = 0
            for i in range(len(caminho) - 1):
                cidade_atual = caminho[i]
                proxima_cidade = caminho[i + 1]
                distancia_total += grafo[cidade_atual][proxima_cidade]
            
            return caminho, distancia_total

        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados: 
                visitados.add(vizinho)
                fila.append(caminho + [vizinho])
                
    return None, 0

grafo_cidades = {
    "São Paulo": {
        "Rio de Janeiro": 400,
        "Curitiba": 410
    },
    "Rio de Janeiro": {
        "São Paulo": 400,
        "Belo Horizonte": 440
    },
    "Curitiba": {
        "São Paulo": 410,
        "Florianópolis": 300
    },
    "Belo Horizonte": {
        "Rio de Janeiro": 440,
        "Brasília": 720
    },
    "Florianópolis": {
        "Curitiba": 300
    },
    "Brasília": {
        "Belo Horizonte": 720
    }
}

if __name__ == "__main__":
    origem = input("Cidade de origem: ").strip()
    destino = input("Cidade de destino: ").strip()

    caminho, distancia = bfs(grafo_cidades, origem, destino)
    
    if caminho:
        print(f"O percurso é: {caminho}")
        print(f"O número de etapas é {len(caminho) - 1}")
        print(f"Distância total: {distancia} km")
        
    else:
        print("Não existe caminho entre as duas cidades nesse grafo.")