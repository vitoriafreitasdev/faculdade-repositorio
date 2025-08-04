class Conta:
    #função para inicializar
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    #função para depositar
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Valor inválido para depósito.")
     #função para sacar
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def exibir_informacoes(self):
        print(f"Titular: {self.nome}\nSaldo: R${self.saldo:.2f}")

conta= Conta("Fernado Alves", 3000)
conta.depositar(1000)
conta.sacar(500)
conta.exibir_informacoes()
