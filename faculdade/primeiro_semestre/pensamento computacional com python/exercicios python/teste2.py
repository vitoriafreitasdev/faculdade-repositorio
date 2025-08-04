#nome = input("Qual é o seu nome: ")
#ano = int(input("Qual ano você vem: "))
#print(f"Seu nome é {nome}")
#print(f"E você veio desse ano: {ano}")

viagens = int(input("Quantas viagens você irá fazer: "))
viagens_cadastradas = 0

for i in range(1, viagens + 1):
    passado_futuro = input("Será passado ou futuro: ")
    viagens_cadastradas += 1

print(f"Número de viagesn: {viagens_cadastradas}")

#Enquanto a idade for menor que 0 vai continuar no loop
while True:
    idade = int(input("Sua idade: "))
    if idade >= 0:
        print("Acesso permitido!")
        break
    else:
        print("Idade inválida, tente novamente.")

#Irá sair do loop quando o usuário apertar 0.
while True:
    print("Opções: ")
    opcoes = int(input("1 - Registrar evento histórico 2 - Mostrar lista de eventos, 0 - Sair"))
    if opcoes == 0:
        break
    else:
        continue