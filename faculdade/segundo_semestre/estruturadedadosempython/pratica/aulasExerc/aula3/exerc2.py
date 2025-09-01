from collections import deque
def bfs(grafo, origem, destino):
    fila = deque([[origem]])
    visitados = {origem}

    while fila: 
        caminho = fila.popleft()
        atual = caminho[-1]
        print("caminho: ", caminho)
        print("atual: ", atual)

        if atual == destino:
            return caminho

        for vizinho in grafo.get(atual, []):
            if vizinho not in visitados: 
                visitados.add(vizinho)
                fila.append(caminho + [vizinho])

    return None
    

grafo_cidades = {
    "São Paulo": ["Rio de Janeiro", "Curitiba"],
    "Rio de Janeiro": ["São Paulo", "Belo Horizonte"],
    "Curitiba": ["São Paulo", "Florianópolis"],
    "Belo Horizonte": ["Rio de Janeiro", "Brasília"],
    "Floarianópolis": ["Curitiba"]
}



if __name__ == "__main__":
    origem = input("Cidade de origem: ").strip()
    destino = input("Cidade de destino: ").strip()

    caminho = bfs(grafo_cidades, origem, destino)

    if caminho:
        print(f"O percurso é: {caminho}")
        print(f"O número de etapas é {len(caminho) - 1}.")
    else:
        print("Não existe caminho entre as duas cidades nesse grafo.")