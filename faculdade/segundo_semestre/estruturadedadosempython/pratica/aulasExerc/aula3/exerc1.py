class Node:
    def __init__(self, valor): 
        self.valor = valor 
        self.filhos = []
    
    def add_child(self, *novos_filhos):
        self.filhos.extend(novos_filhos)

def imprimir_arvore(no, nivel=0):
    indent = "" * (4 * nivel)
    print(f"{indent}- {no.valor}")
    for filho in no.filhos:
        imprimir_arvore(filho, nivel + 1)

anakin = Node("Anakin Skywalker")
luke = Node("Luke Skywalker")
leia = Node("Leia Skywalker")
ben = Node("Ben Solo")

leia.add_child(ben)
anakin.add_child(luke, leia)

if __name__ == "__main__":
    imprimir_arvore(anakin)