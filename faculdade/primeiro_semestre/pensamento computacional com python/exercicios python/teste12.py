class Evento:
    def __init__(self, ano, descricao):
        self.ano = ano
        self.descricao = descricao

    def __str__(self):
        return f"Ano {self.ano}: {self.descricao}"

class Viajante:
    def __init__(self, nome):
        self.nome = nome
        self.eventos_vividos = []

    def registrar(self, evento):
        self.eventos_vividos.append(evento)
        print(f"{self.nome} registrou: {evento}")

    def relatorio_pos_viagem(self):
        print(f"RELATÓRIO DE {self.nome.upper()} ")
        for evento in self.eventos_vividos:
            print(evento)

class MaquinaDoTempo:
    def __init__(self, modelo):
        self.modelo = modelo

    def viajando(self, viajante, ano, descricao_evento):
        print(f"\nViajando para o ano {ano} com a máquina {self.modelo}...")
        evento = Evento(ano, descricao_evento)
        viajante.registrar(evento)

viajante = Viajante("Vitoria")
maquina = MaquinaDoTempo("MX-YZ14")

maquina.viajando(viajante, 2050, "Tecnologia novas")
maquina.viajando(viajante, 3040, "Mundo Novo")
viajante.relatorio_pos_viagem()

