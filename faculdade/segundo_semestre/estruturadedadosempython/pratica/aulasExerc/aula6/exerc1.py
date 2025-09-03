import heapq 

tarefa = []

heapq.heappush(tarefa, (3, "Enviar relatório."))
heapq.heappush(tarefa, (1, "Responder e-mails"))
heapq.heappush(tarefa, (2, "Revisar código"))

while tarefa:
    prioridade, nome = heapq.heappop(tarefa)
    print(prioridade, nome)