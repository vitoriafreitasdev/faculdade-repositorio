

ano = int(input("Incira o ano atual: "))


destino = int(input("Insira o ano de destino da viagem no tempo: "))


dif_anos = ano - destino


if dif_anos > 0:

    print(f"Voce viajará {dif_anos} anos para o futuro")

elif dif_anos < 0:

    print(f"Voce viajará {abs(dif_anos)} anos para o passado")

else:

    print("Voce permanecerá no ano atual")


n = float(input("n1: "))

n2 = float(input("n2: "))

div = n / n2

print(f"{div}")


mensagem = input("Insira a mensagem a ser enviada através dos séculos")

mensagemLimp = mensagem.strip()

mensagemForm = mensagemLimp.title()

mensagemUnicode = mensagemForm.replace("Tempo", "TEMPO")

mensagemFinal = mensagemUnicode + "" + "⌛"

print("Mensagem através das eras", mensagemFinal)

anoDestino = 2050

coordenadas = (51.5074, -0.1278)

modoDeViagem = "instantaneo"

print("Configurações da máquina do tempo:")
print("Ano de destino:", anoDestino)
print("Coordenadas de destino:", coordenadas)
print("Modo de viagem:", modoDeViagem)


ano_presente = 2030

ano1 = int(input("Insira o primeiro ano: "))

ano2 = int(input("Insira o segundo ano: "))

distancia_ano1 = abs(ano1 - ano_presente)

distancia_ano2 = abs(ano2 - ano_presente)

if distancia_ano1 > distancia_ano2:
    print(f"O ano {ano1} está mais distante do presente do que o ano {ano2}.")
elif distancia_ano2 > distancia_ano1:
    print(f"O ano {ano2} está mais distante do presente do que o ano {ano1}.")
else:
    print(f"Os anos {ano1} e {ano2} estão igualmente distantes do presente.")



from datetime import datetime


anoAtual = datetime.now().year


anoDestino = int(input("Insira o ano destino: "))


intervalo = anoDestino - anoAtual


print("O intervalo de tempo entre", anoAtual, "e", anoDestino, "é de", intervalo, "anos.")


def inteiro_para_romano(numero):
# Mapeamento de números inteiros para numerais romanos
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    romano = ""


    for valor, numeral in valores:
        while numero >= valor:
            romano += numeral
            numero -= valor

    return romano


# Solicita ao usuário que insira o ano de destino
ano_destino = int(input("Insira o ano de destino: "))
# Determina a década
# Ao dividir o ano por 10 (inteiro) e multiplicar novamente por 10, obtemos a década base.
# Por exemplo, 1995 // 10 = 199, 199 * 10 = 1990, logo, a década é a de 1990.
decada = (ano_destino // 10) * 10
# Determina o século
# O primeiro século vai do ano 1 ao ano 100, o segundo do ano 101 ao 200, e assim por diante.
# A fórmula (ano - 1) // 100 + 1 calcula corretamente o século.
# Por exemplo, para o ano 2030: (2030 - 1) // 100 + 1 = (2029
#// 100) + 1 = 20 + 1 = 21, século XXI.
seculo = inteiro_para_romano((ano_destino - 1) // 100 + 1)
# Exibe o resultado
print(f"O ano {ano_destino} pertence à década de {decada} e ao século {seculo}.")
