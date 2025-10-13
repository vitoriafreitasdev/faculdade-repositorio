
from collections import deque 

pilha = []
pilha.append("prato 1")
pilha.append("prato 2")
print(pilha.pop())

fila = deque()
fila.append("cliente 1")
fila.append("cliente 2")
print(fila.popleft())

###

import time 

fila = deque()
pilha = []
t0 = time.time() 
for i in range(3):
    nome = input("Nome do cliente: ")
    fila.append(nome)

print("\n Iniciando atendimentos.")

while fila:
    cliente = fila.popleft()
    print(f"Atendendo {cliente}")

for i in range(3):
    tarefa = input(f"Tarefa {i+1}: ")
    pilha.append(tarefa)

print(f"\nExecutando tarefa {i+1}")

while pilha:
    print(f"Executando: {pilha.pop()}")
t1 = time.time()

tempo_de_execucao = t1 - t0 
print("Tempo de execução: ", tempo_de_execucao)
