# def soma(lista):
#     total = 0
#     for x in lista:
#         total += x
#     return total

# print(soma([1, 2, 3, 4]))

def somaRecursiva(lista):
    soma = 0
    caso_base = 0
    if len(lista) == 0:
        return 0 # se a lista estiver vazia retorne
    else:
        soma = lista[caso_base] + somaRecursiva(lista[1:]) # pegue o primeiro elemento e soma com o restante da lista
        return soma
                
    
print(somaRecursiva([1, 2, 3, 4]))

         