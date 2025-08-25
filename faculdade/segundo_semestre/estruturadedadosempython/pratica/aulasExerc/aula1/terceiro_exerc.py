from collections import deque 

fila = deque()
pilha = []

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