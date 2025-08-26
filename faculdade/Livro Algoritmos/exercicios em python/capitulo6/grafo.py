from collections import deque 

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["tom", "johnny"] 
grafo["anuj"] = []
grafo["peggy"] = []
grafo["tom"] = []
grafo["johnny"] = []

def pessoa_e_vendendor(nome):
    return nome[-1] == 'm'

def pesquisa_em_largura():
    # Cria a fila localmente
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo["voce"]
    verificadas = []
    
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas: 
            if pessoa_e_vendendor(pessoa):
                print(pessoa + " é um vendendor")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)
    return False

pesquisa_em_largura()