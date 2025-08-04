ARQUIVO_REGISTROS = "registros.txt"
#função para salvar
def salvar(ano, descricao):
    with open(ARQUIVO_REGISTROS, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f"{ano}|{descricao}\n")
#função para ler
def ler():
    try:
        with open(ARQUIVO_REGISTROS, 'r', encoding='utf-8') as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        return []
#função para gerenciar

while True:
    print("\nGERENCIADOR DE VIAGENS")
    print("1. Registrar nova viagem")
    print("2. Ver todas as viagens")
    print("3. Sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        ano = input("Ano visitado: ")
        descricao = input("Descrição: ")
        salvar(ano, descricao)
        print("Viagem registrada!")
    elif opcao == "2":
        registros = ler()
        if not registros:
            print("Nenhuma viagem registrada ainda.")
        else:
            print("\nREGISTROS")
            for linha in registros:
                ano, descricao = linha.strip().split('|')
                print(f"Ano {ano}: {descricao}")
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
