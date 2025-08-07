musicas = {
    "Justin Bieber": 141,
    "Mariah carey": 233,
    "Black Sabbath": 34,
    "Queen": 56,
    "Alice in chains": 76,
    "Aretha Franklin": 29,
    "Nirvana": 30
}

# for musica in musicas:
#     print(musicas[musica])

arr = []

for musica in musicas:
    arr.append(musicas[musica])



def buscarMaior(arr):
    maior = arr[0]
    maior_indice = 0
    for i in range(1, len(arr)):
        if arr[i] > maior:
            maior = arr[i]
            maior_indice = i 
    return maior_indice

mais_escutados = []

def ordernar(arr):
    for i in range(len(arr)):
        maior = buscarMaior(arr)
        mais_escutados.append(arr.pop(maior))
    

ordernar(arr)

print(mais_escutados)
# terminar criar um novo objeto com dos artistas mais escutados para os menos
# def buscarMenor(arr):
#     menor = arr[0]
#     menor_indice = 0
#     for i in range(1, len(arr)):
#         if arr[i] < menor:
#             menor = arr[i]
#             menor_indice = i
#     return menor_indice

# def ordenarporselacao(arr):
#     novoArr = []
#     for i in range(len(arr)):
#         menor = buscarMenor(arr)
#         novoArr.append(arr.pop(menor))
#     return novoArr

# print(ordenarporselacao(arr))

