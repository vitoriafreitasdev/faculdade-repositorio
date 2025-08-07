
pessoa1 = {}
pessoa2 = {}


pessoa1['idade'] = 30
pessoa1['profissão'] = "arquiteto"

pessoa2['idade'] = 22
pessoa2['profissão'] = "professor"


class MeuObjeto:
    def __init__(self, valor):
        self.valor = valor

lista_de_objetos = []
objeto1 = MeuObjeto(pessoa1)
objeto2 = MeuObjeto(pessoa2)

lista_de_objetos.append(objeto1)
lista_de_objetos.append(objeto2)

# Iterando sobre a lista e acessando os objetos
for objeto in lista_de_objetos:
    print(objeto.valor)

# Usando extend para adicionar múltiplos objetos
lista_de_objetos.extend([MeuObjeto("objeto 3"), MeuObjeto("objeto 4")])
print([o.valor for o in lista_de_objetos])


for objeto in lista_de_objetos:
    valor = objeto.valor
    if isinstance(valor, dict) and 'idade' in valor: 
        print(valor['idade'])


l = {}

l['nome'] = "Paulo"
l['idade'] = 30 
l['altura'] = 1.75
