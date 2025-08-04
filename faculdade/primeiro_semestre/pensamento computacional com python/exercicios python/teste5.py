def calcular(distancia_anos, velocidade_segundo):
    #calcular em segundos
    tempo_segundos = distancia_anos / velocidade_segundo
    return tempo_segundos

def converter(tempo_segundos):
    #converter em minutos e horas
    tempo_minutos = tempo_segundos / 60
    tempo_horas = tempo_minutos / 60
    return tempo_minutos, tempo_horas


distancia = float(input("Digite a distância da viagem (em anos): "))
velocidade = float(input("Digite a velocidade da viagem (em anos/segundo): "))

segundos = calcular(distancia, velocidade)

minutos, horas = converter(segundos)
    
print(f"\nTempo de viagem:")
print(f"- Segundos: {segundos:.2f} s")
print(f"- Minutos: {minutos:.2f} min")
print(f"- Horas: {horas:.2f} h")

