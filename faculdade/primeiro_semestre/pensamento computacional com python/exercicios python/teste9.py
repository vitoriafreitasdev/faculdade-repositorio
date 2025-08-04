from datetime import datetime

def dias_para_viagem(data_viagem_str):
    hoje = datetime.now()
    data_viagem = datetime.strptime(data_viagem_str, "%d/%m/%Y")
    diferenca = data_viagem - hoje 
    #print(f"Hoje", hoje)
    #print(f"Viagem", data_viagem)
    #print(f"Diferença", diferenca)

    return diferenca.days
#exemplo de uso
print(dias_para_viagem("30/12/2025"))
