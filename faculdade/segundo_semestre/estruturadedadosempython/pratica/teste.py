
# class No:
#     def __init__(self, dado, esq=None, dir=None):
#         self.dado = dado
#         self.esq = esq 
#         self.dir = dir 
    
# def em_ordem(raiz, visita=None):
#     if visita is None:
#         visita = []
#     if raiz:
#         em_ordem(raiz.esq, visita)
#         visita.append(raiz.dado)
#         em_ordem(raiz.dir, visita)
#     return visita


# no_a = No("A")
# no_j = No("J")
# no_e = No("E", no_a, no_j)
# no_r = No("R")
# no_y = No("Y", no_r)
# raiz = No("M", no_e, no_y)

# print(" ".join(em_ordem(raiz)))

lista = [2, 4, 6, 8]
n = len(lista)

mediana = lista[n//2] if n % 2 else (lista[n//2-1] + lista[n//2])/2
print(mediana)
