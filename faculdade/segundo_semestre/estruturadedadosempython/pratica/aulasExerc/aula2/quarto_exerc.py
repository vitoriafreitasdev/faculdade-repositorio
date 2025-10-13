
from collections import deque

fila = deque()

fila.append("Cliente A")
fila.append("Cliente B")
fila.append("Cliente C")
# utilizando o popleft, pois é mais eficiente que o pop(0)
atendido = fila.popleft()

print("Atendido: ", atendido)
print("fila agora: ", list(fila))

fila.append("Cliente D")
print("Proximo a ser atendido", fila[0])