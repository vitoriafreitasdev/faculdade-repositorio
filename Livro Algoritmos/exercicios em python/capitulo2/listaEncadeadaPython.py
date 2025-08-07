# lista = []

# lista.insert(0, 'ygor')
# lista.insert(0, 'jorge')

# print(lista)
# lista.append('joão')
# print(lista)

# listaPython = list(range(10))
# print(listaPython)
# print(listaPython[2])
# listaPython[3] = 4
# print(listaPython)
# print(listaPython[5:10])

# listaTeste = []

# listaTeste.insert(0, 5)
# listaTeste.insert(1, 20)
# listaTeste.insert(2, 15)
# listaTeste.insert(2, 7)

# print(listaTeste[-1:-2:-1])
# print(listaTeste)

# lista3 = list(range(10))

# del lista3[4]

# print(lista3)

# l = [0, 1, 2, 3, 4]
# l.pop(4)
# print(l)

# lista[2] = 10

# print(lista)

lista1 = list(range(10, 20))

lista2 = list(range(55, 60))

print(lista1)
print(lista2)

lista1.extend(lista2)
print(lista1)

lista1.pop()
print(lista1)

lista = ['joão', 'maria', 'josé', 'ana', 'carlos', 'maria','juliana']
revertida = reversed(lista)
print(revertida)
lista.reverse()
print(lista)