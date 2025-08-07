
from hashlib import sha256
from math import ceil 

class TabelaHash:
    class __Elemento:
        def __init__(self, chave, valor):
            self.chave = chave 
            self.valor = valor 

        def __str__(self):
            return f'{self.chave}: {self.valor}'
        
        def __repr__(self):
            return self.__str__()
    def __init__(self):
        self.__capacidade_atual = 5 # capacidade/tamanho da tabela interna
        self.__tabela_interna = [[] for _ in range(self.__capacidade_atual)]
        self.__tamanho = 0 # quantidade de elementos salvos na tabela hash

        self.__limiar_expandir = 0.75 #quando ultrapassar os 80% da capacidade vai expandir
        self.__fator_expasao = 2 # vai dobrar a capacidade
        self.__limiar_reduzir = 0.20 #quando chegar em 20 porcento vai dimuir
        self.__fator_reducao = 0.5 #dividir a capacidade ao meio

    def __str__(self):
        retorno = '{'
        total = len(self)
        i = 0
        for k, v in self: 

            if isinstance(k, str):
                retorno += f"'{k}: '"
            else:
                retorno += f'{k}: '

            if isinstance(v, str):
                retorno += f"'{v}'"
            else:
                retorno += f'{v}'

            if i < total - 1:
                retorno += ', '
            i += 1
    
        retorno += '}'

        return retorno
    def __repr__(self):
        return self.__str__()
    def __len__(self):
        return self.__tamanho
    # fator de carga => quantos porcento da ocupado
    @property
    def __fator_carga(self):
        return self.__tamanho / self.__capacidade_atual
    @staticmethod
    def __verificar_chave(chave):
        hash(chave)

    @staticmethod
    def __hash_determinisco(chave):
        codificacao = str(chave).encode()
        return int(sha256(codificacao).hexdigest(), 16) # para transformarmar em base dez
    
    def __descobrir_indice(self, chave):
        return self.__hash_determinisco(chave) % self.__capacidade_atual # => não pode usar a função hash padrao do python, pois nao é determinisca(quando recarregar o arquivo vai dar um valor diferente)
        pass
    def __setitem__(self, chave, valor):
        self.__verificar_chave(chave)

        indice = self.__descobrir_indice(chave)
        #verifica se a chave ja existe na tabela
        for elemento in self.__tabela_interna[indice]:
            if elemento.chave == chave:
                elemento.valor = valor # se encontrar atualiza o valor
                return

        # Se não encontrar, adiciona um novo elemento
        novo_elemento = self.__Elemento(chave, valor)
        self.__tabela_interna[indice].append(novo_elemento)
        self.__tamanho += 1

    def __iter__(self):
        for lista in self.__tabela_interna:
            for elemento in lista: 
                yield elemento.chave, elemento.valor

    def __getitem__(self, chave):
        self.__verificar_chave(chave)

        if self.__fator_carga >= self.__limiar_expandir:
            self.__atualizar_tabela(self.__capacidade_atual * self.__fator_expasao)


        indice = self.__descobrir_indice(chave)

        for elemento in self.__tabela_interna[indice]:
            if elemento.chave == chave:
                return elemento.valor

        raise KeyError(f'Chave {chave} não encontrada.')
    
    def __delitem__(self, chave):
        self.__verificar_chave(chave)

        if self.__fator_carga <= self.__limiar_reduzir:
            self.__atualizar_tabela(ceil(self.__capacidade_atual * self.__fator_reducao))

        indice = self.__descobrir_indice(chave)

        for i, elemento in enumerate(self.__tabela_interna[indice]):
            if elemento.chave == chave:
                del self.__tabela_interna[indice][i]
                self.__tamanho -= 1
                return
            
        raise KeyError(f'Chave {chave} não encotrado')
    
    def __atualizar_tabela(self, nova_capacidade):
        tabela_antiga = self.__tabela_interna

        self.__tabela_interna = [[] for _ in range(nova_capacidade)]
        self.__capacidade_atual = nova_capacidade
        self.__tamanho = 0

        for lista in tabela_antiga:
            for elemento in lista:
                self[elemento.chave] = elemento.valor

pessoa = TabelaHash()
pessoa['nome'] = 'João da Silva'
pessoa['idade'] = 30
pessoa['sexo'] = 'Masculino'
pessoa['profissão'] = 'Programador'
pessoa['nacionadade'] = 'Brasileira'
pessoa['salario'] = 12500.00
pessoa['estado_civil'] = 'Solteiro'
pessoa['cor'] = 'Pardo'
pessoa['altura'] = 1.75
pessoa['peso'] = 80.00
pessoa['cor_olhos'] = 'Castanho'
pessoa['cor_cabelo'] = 'Castanho'
pessoa['endereço'] = 'Rua das Flores, 123'
pessoa['cidade'] = 'São Paulo'
pessoa['estado'] = 'SP'
pessoa['pais'] = 'Brasil'
pessoa['tipo_sanguineo'] = 'O+'
pessoa['cep'] = '12345-123'
pessoa['telefone'] = '(11)99999-9999'
pessoa['email'] = 'email@email.com'
pessoa['cpf'] = '123.456.789-10'
pessoa['rg'] = '12.345.678-9'
pessoa['titulo_eleitor'] = '1234 5678 9012'





del pessoa['nome'] 
del pessoa['idade'] 
del pessoa['sexo'] 
del pessoa['profissão'] 
del pessoa['nacionadade'] 
del pessoa['salario'] 
del pessoa['estado_civil'] 
del pessoa['cor'] 
del pessoa['altura'] 
del pessoa['peso'] 
del pessoa['cor_olhos'] 
del pessoa['cor_cabelo']
del pessoa['endereço']
del pessoa['cidade'] 
del pessoa['estado'] 
del pessoa['pais'] 
del pessoa['tipo_sanguineo'] 
del pessoa['cep'] 
del pessoa['telefone']
del pessoa['email'] 
del pessoa['cpf'] 
del pessoa['rg'] 
del pessoa['titulo_eleitor']

print(f'Quantidade de elementos: {len(pessoa)}')
print(pessoa)




















# print(f'Nome: {pessoa["nome"]}')
# print(f'Profissão: {pessoa["profissão"]}')
# print(f'Salário: {pessoa["salario"]}')

# print(f'Quantidade de elementos: {len(pessoa)}')

# for k, v in pessoa:
#     print(f'{k} = {v}')

# del pessoa['salario']
# print('Apagamos o salário')

# for k, v in pessoa:
#     print(f'{k} = {v}')


# print(f'Quantidade de elementos: {len(pessoa)}')
