import os

meses_sistema = ["dez2022", "jan2022", "out2022", "fev2022", "mai2022", "set2022", "nov2022", "set2020", "out2021", "jan2019"]


arquivos_extraidos = []

def pegar_arquivos_pasta(pasta):
    lista_arquivos = os.listdir(pasta)
    # se tiver txt e vencdas no nome do arquivo então eu vou pegar o mes
    
    for arquivo in lista_arquivos:
        if ".txt" in arquivo and "Vendas" in arquivo:
            #significa que eu quero pegar o nome do mes
            nome_mes = arquivo.split()[-1].replace(".txt", "") # split divide a string entre os espaço e transforma em um array. Exemplo ["Compras", "-", "ago2022.txt"]. O [-1] para pegar o ultimo elemento desse array
            arquivos_extraidos.append(nome_mes)
        elif ".txt" not in arquivo: # se é uma pasta
            pegar_arquivos_pasta(f"{pasta}/{arquivo}")

pegar_arquivos_pasta("arquivos")
print(arquivos_extraidos)

for mes in meses_sistema:
    if mes not in arquivos_extraidos:
        print(mes)