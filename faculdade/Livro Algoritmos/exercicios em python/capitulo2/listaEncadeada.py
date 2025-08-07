
class Lista: 
    class No: 
        def __init__(self, valor, proximo=None):
            self.valor = valor 
            self.proximo = proximo

        def __str__(self):
            return str(self.valor)
        
    def __init__(self, iteravel=None):
        self.__cabeca = None 
        self.__cauda = None
        self.__quantidade = 0
        #para ver se objeto tem o atributo iter
        if iteravel is not None and hasattr(iteravel, '__iter__'):
            for item in iteravel:
                self.inserir_no_fim(item)
        elif iteravel is not None:
            raise TypeError(f'O objeto {type(iteravel)} não é iteravel.')
    def __len__(self):
        return self.__quantidade
    #para transformar a lista em string, e poder mostrar ela na tela (print(lista))
    def __str__(self):
        return '[' + ', '.join([str(valor) for valor in self]) + ']'
    # repr =. representação interna
    def __repr__(self):
        return self.__str__

    # para fazer a busca de todos elemento (mais eficiente, pois pelo getitem sempre volta da cabeca, esse aqui com o yield não) => algoritmo lazy  evolution
    def __iter__(self):
        atual = self.__cabeca
        while atual is not None: 
            yield atual.valor # yield retorna esse valor, yield pausa a função, quando for solicitar novamente ela nao vai voltar do inicio
            atual = atual.proximo
    #para fazer a busca individualmente
    def __delitem__(self, posicao):
        if posicao < 0:
            posicao = len(self) + posicao
        
        if posicao < 0 or posicao >= self.__quantidade:
            raise IndexError('Posição inválida.')
        
        self.__quantidade -= 1

        if posicao == 0:
            self.__cabeca = self.__cabeca.proximo
            if self.__cabeca is None:
                self.__cauda = None
            return
        
        i = 0
        atual = self.__cabeca
        # buscando o elemento anterior a posição que a gente quer remover
        while atual.proximo is not None and i < posicao - 1:
            atual = atual.proximo
            i += 1
        
        # removendo da cauda
        if atual.proximo == self.__cauda:
            self.__cauda = atual 

        # removendo o elemento desejado 
        atual.proximo = atual.proximo.proximo
    def __setitem__(self, posicao, valor):
        if posicao < 0:
            posicao = len(self) + posicao
        if posicao < 0 or posicao >= self.__quantidade:
            raise IndexError('Posição inválida.')
        
        atual = self.__cabeca
        for i in range(posicao):
            atual = atual.proximo
        atual.valor = valor
    def __getitem__(self, posicao):
        #para poder fazer o fatiamento
        if isinstance(posicao, slice):
            passo = posicao.step if posicao.step is not None else 1

            if passo == 0:
                raise ValueError('Passo não pode ser zero.')

            # inicio = posicao.start if posicao.start is not None else (0 if passo > 0 else len(self) - 1)
            # fim = posicao.stop if posicao.stop is not None else (len(self) if passo > 0 else -1)

            # if inicio < 0:
            #     inicio += len(self)
            # if fim < 0:
            #     fim += len(self)

            if passo > 0:
                inicio = posicao.start if posicao.start is not None else 0
                fim = posicao.stop if posicao.stop is not None else len(self)
            else:
                inicio = posicao.start if posicao.start is not None else len(self) -1
                fim = posicao.stop if posicao.stop is not None else -1
            
            if inicio < 0:
                inicio - len(self) + inicio

            if fim < 0 and posicao.stop is not None:
                fim = len(self) + fim

            fatia = Lista()
            # se passo for positiva, vamos usar lazy evaluation com __iter__
            if passo > 0:
                i = 0 
                indices = range(inicio, fim, passo)
                it = iter(self)
                while i < fim:
                    v = next(it)
                    if i in indices:
                        fatia.inserir_no_fim(v)
                    i+= 1
            else: # se for negativo, vamos user __getitem__
                for i in range(inicio, fim, passo):
                    fatia.inserir_no_fim(self[i])

            return fatia
        
        if posicao < 0:
            posicao = len(self) + posicao

        if posicao < 0 or posicao >= self.__quantidade: 
            raise IndexError('Posição inválida')
        
        # buscando o elemento que está ma posição desejada
        atual = self.__cabeca 
        for i in range(posicao):
            atual = atual.proximo 

        return atual.valor 

    def inserir_no_fim(self, valor):
        novo = self.No(valor)
        self.__quantidade +=1

        if self.__cabeca is None:
            self.__cabeca = novo
            self.__cauda = novo
            return
       
        self.__cauda.proximo = novo 
        self.__cauda = novo
       

    def inserir(self, posicao, valor):

        novo = self.No(valor)
        self.__quantidade += 1

        # quando a lista é vazio
        if self.__cabeca is None:
            self.__cabeca = novo
            self.__cauda = novo
            return
        
        # inserir na cabeça (primeira posição)
        if posicao <= 0:
            novo.proximo = self.__cabeca
            self.__cabeca = novo
            return
        
        i = 0
        atual = self.__cabeca
        # buscando o elemento anterior a posição que a gente quer inserir
        while atual.proximo is not None and i < posicao - 1:
            atual = atual.proximo
            i += 1

        if atual.proximo is None:
            self.__cauda = novo

        novo.proximo = atual.proximo
        atual.proximo = novo 

    def estender(self, iteravel):
        if iteravel is None or not hasattr(iteravel, '__iter__'):
            raise TypeError(f'O objeto {type(iteravel)} não é iteravel.')
        
        for item in iteravel:
            self.inserir_no_fim(item)

    def remover(self, valor):
        posicao = self.indice(valor)
        del self[posicao]

    def indice(self, valor):
        i = 0
        atual = self.__cabeca
        while atual is not None:
            if atual.valor == valor:
                return i 
            atual = atual.proximo
            i += 1
        
        raise ValueError(f'{valor} não está na lista.')
    
    def pop(self, posicao=None):
        if posicao is None:
            posicao = len(self) - 1 # remove e retornar o último elemento da lista
        
        valor = self[posicao]
        del self[posicao]
        return valor

    def limpar(self):
        self.__cabeca = None 
        self.__cauda = None 
        self.__quantidade = 0

    def contar(self, valor):
        contador = 0

        for elemento in self:
            if elemento == valor:
                contador += 1

        return contador

    def __reversed__(self):
        return self[::-1]

    # in place
    def reverter(self):

        revertido = reversed(self)
        self.limpar()
        self.estender(revertido)

    def copiar(self):
        return self[:]

lista = Lista(['joão', 'maria', 'josé', 'ana', 'carlos', 'maria','juliana'])
copiada = lista.copiar()
print(lista)
print(copiada)
print(id(lista))
print(id(copiada))
