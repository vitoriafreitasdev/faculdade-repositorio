from collections import deque


#grafo = {}
#grafo["voce"] = ["alice", "bob", "claire"]
#grafo["bob"] = ["anuj", "peggy"]
#grafo["alice"] = ["peggy"]
#grafo["claire"] = ["thom", "jonny"]
#grafo["anuj"] = []
#grafo["peggy"] = []
#grafo["thom"] = []
#grafo["jonny"] = []


grafo = {
    "voce": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

def pessoa_e_vendedor(nome):
    return  nome[-1] == 'm'

fila_de_pesquisa = deque()
fila_de_pesquisa += grafo["voce"]



def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(f"{pessoa} é um vendedor de manga!")
                return True
        else:
            fila_de_pesquisa += grafo[pessoa]
            verificadas.append(pessoa)
    return False

pesquisa("voce")