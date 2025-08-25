from collections import deque

fila = deque()

fila.append("Cliente A")
fila.append("Cliente B")
fila.append("Cliente C")

atendido = fila.popleft()

print("Atendido: ", atendido)
print("fila agora: ", list(fila))

fila.append("Cliente D")
print("Proximo a ser atendido", fila[0])