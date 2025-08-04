# Verificação de permissão temporal
while True:
    try:
        idade = int(input("Qual é a sua idade? "))
        if idade >= 0:
            break  # Sai do while
        else:
            print("Por favor, insira uma idade válida.")
    except ValueError:
        print("Por favor, insira um número válido.")

if idade < 18:
    print("Acesso negado.")
    exit()  # Encerra o programa se a idade for menor que 18
else:
    print("Acesso permitido.")

# Pergunta quantas viagens no tempo deseja fazer
while True:
    try:
        viagens = int(input("Quantas vezes você deseja viajar no tempo? "))
        if viagens > 0:
            break
        else:
            print("Por favor, insira um número válido de viagens.")
    except ValueError:
        print("Por favor, insira um número inteiro.")

# Lista para armazenar as viagens
registro_viagens = []

# Solicitação dos detalhes das viagens
for i in range(1, viagens + 1):
    ano = input(f"Digite o ano alvo da viagem {i}: ")

    while True:
        direcao = input("Será para o 'passado' ou 'futuro'? ").strip().lower()
        if direcao in ["passado", "futuro"]:
            break
        else:
            print("Opção inválida! Digite 'passado' ou 'futuro'.")

    registro_viagens.append((ano, direcao))  # Adiciona a viagem à lista

# Lista de eventos históricos
eventos_historicos = []

# Menu de opções para eventos históricos
while True:
    print("\nMenu de Opções:")
    print("1 - Registrar evento histórico")
    print("2 - Mostrar lista de eventos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        evento = input("Descreva o evento histórico: ")
        eventos_historicos.append(evento)
        print("Evento registrado com sucesso!")

    elif opcao == "2":
        if eventos_historicos:
            print("\nLista de eventos históricos registrados:")
            for idx, evento in enumerate(eventos_historicos, start=1):
                print(f"{idx}. {evento}")
        else:
            print("Nenhum evento registrado ainda.")

    elif opcao == "0":
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida! Tente novamente.")

# Exibição do resumo das viagens
nome = input("\nInforme seu nome para o resumo: ")
print(f"\nOlá, {nome}! Aqui está o resumo das suas viagens no tempo:")
for i, (ano, direcao) in enumerate(registro_viagens, start=1):
    print(f"Viagem {i}: {direcao.capitalize()} para o ano {ano}.")



