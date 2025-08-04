from datetime import datetime

def preparar(destino):
    ano_atual = datetime.now().year
    diferenca = abs(destino - ano_atual) # vai retornar um valor absoluto
    energia_necessaria = diferenca * 10  
    return diferenca, energia_necessaria

def executar(energia_necessaria, energia_disponivel=100):
    #se tiver energia retorna verdadeiro, se não retorna falso
    if energia_disponivel >= energia_necessaria:
        return True
    else:
        return False

def verificar_chegada(destino, viagem_bem_sucedida):

    if viagem_bem_sucedida:
        print(f"Viagem bem-sucedida! Você chegou ao ano {destino}.")
    else:
        print("Falha na viagem! Energia insuficiente.")

def viagem_tempo():
    destino = int(input("Digite o ano de destino para a viagem no tempo: "))
    
    diferenca, energia_necessaria = preparar(destino)
    print(f"Preparando viagem para {destino}...")
    print(f"Diferenca de anos: {diferenca}, Energia necessária: {energia_necessaria}")
    
    viagem_bem_sucedida = executar(energia_necessaria)
    
    verificar_chegada(destino, viagem_bem_sucedida)

# Executar o organizador de viagem no tempo
viagem_tempo()