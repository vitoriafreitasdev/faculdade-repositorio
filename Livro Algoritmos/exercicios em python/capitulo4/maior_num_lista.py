
# def maior(lista):
#     maior = lista[0]
#     for i in lista:
#         if i >= maior:
#             maior = i
#     return maior

# print(maior([3, 4, 6, 7, 8]))

def maior(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] >= maior:
            maior = lista[i]
    return maior


# recursiva agora
print(maior([4, 6, 7, 8]))


def maior_recursiva(lista):
    if len(lista) == 1:
        return lista[0]
    maior = maior_recursiva(lista[1:])
    return lista[0] if lista[0] > maior else maior 

print(maior_recursiva([ 4, 9, 7]))  
print(maior_recursiva([-1, -5, -3]))      
print(maior_recursiva([5])) 

# sem fatiamento

def maior_recursivo_eficiente(lista, index=0):
    if index == len(lista) - 1:
        return lista[index]
    maior_restante = maior_recursivo_eficiente(lista, index + 1)
    return lista[index] if lista[index] > maior_restante else maior_restante

print(maior_recursivo_eficiente([10, 4, 6, 7, 11])) 