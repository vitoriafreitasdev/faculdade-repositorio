agenda  = {} # guardar os compromissos

quant_compromissos = int(input("Quantos compromissos você irá inserir: "))

for i in range(1, quant_compromissos + 1):
    ano = input("Ano: ")
    compromisso = input("Compromisso: ")
    if ano in agenda:
        agenda[ano].append(compromisso)
    else:
        agenda[ano] = [compromisso]
    print("Compromisso adicionado com sucesso.")

print(f"Agenda: {agenda}")

#todas as girias
giria = {
        "truta": "meu caro",
        "suave": "saudação respeitosa",
        "pego a visão": "compreende",
        "parça": "meu amigo",
        "zoação": "brincadeiras",
    }
#processo de tradução
print(f"Girias: {giria}")
frase_completa = input("Digite uma frase para traduzir: ").lower()
frase_dividida = frase_completa.split()
frase_traduzida = []

for palavra in frase_dividida:
    if palavra in giria:
        frase_traduzida.append(giria[palavra])
    else:
        frase_traduzida.append(palavra)

print("\nFrase traduzida:")
print(" ".join(frase_traduzida))