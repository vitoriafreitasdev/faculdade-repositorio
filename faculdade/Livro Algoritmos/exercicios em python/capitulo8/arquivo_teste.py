
dados = {}

dados_para_inserir = ['Vitoria', 'Julia', 'Davih']


for nome in dados_para_inserir:
    if 'nomes' in dados:
        dados['nomes'].append(nome)
    else:
        dados['nomes'] = [nome]

print(dados)