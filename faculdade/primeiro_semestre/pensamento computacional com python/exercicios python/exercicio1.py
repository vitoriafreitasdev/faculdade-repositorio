anos_visitados = []

while True:
    ano = input("Insira um ano visitado (ou digite sair para finalizar : ")
    if ano.lower() == 'sair':
        break
    else:
        anos_visitados.append(ano)
        print(f"Ano {ano} registrado")


print("\nAnos visitados")
for ano in anos_visitados:
    print(ano)