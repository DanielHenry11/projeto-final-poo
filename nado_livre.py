from modelos.nadador import Nadador
from modelos.atendente import Atendente
from modelos.toalha import Toalha
from modelos.utilizacao import Utilizacao


class NadoLivre:

    def __init__(self):
        self.nadadores = []
        self.atendentes = []
        self.toalhas = []
        self.utilizacoes = []

    def cadastrar_nadador(self, nome, matricula):
        nadador = Nadador(nome, matricula)
        self.nadadores.append(nadador)

    def cadastrar_atendente(self, nome):
        atendente = Atendente(nome)
        self.atendentes.append(atendente)

    def cadastrar_toalha(self, codigo):
        toalha = Toalha(codigo)
        self.toalhas.append(toalha)

    def retirar(self, matricula, codigo, nome_atendente):

        nadador = None

        for n in self.nadadores:
            if n.matricula == matricula:
                nadador = n

        if nadador is None:
            print("Nadador não encontrado.")
            return

        toalha = None

        for t in self.toalhas:
            if t.codigo == codigo:
                toalha = t

        if toalha is None:
            print("Toalha não encontrada.")
            return

        if not toalha.disponivel:
            print("Esta toalha está em uso.")
            return

        atendente = None

        for a in self.atendentes:
            if a.nome.lower() == nome_atendente.lower():
                atendente = a

        if atendente is None:
            print("Atendente não encontrado.")
            return

        toalha.disponivel = False

        utilizacao = Utilizacao(
            nadador,
            toalha,
            atendente
        )

        self.utilizacoes.append(utilizacao)

        print("Retirada realizada com sucesso.")

    def devolver(self, codigo, nome_atendente):

        utilizacao_encontrada = None

        for utilizacao in self.utilizacoes:
            if utilizacao.toalha.codigo == codigo:
                if utilizacao.aberta:
                    utilizacao_encontrada = utilizacao

        if utilizacao_encontrada is None:
            print("Utilização não encontrada.")
            return

        atendente = None

        for a in self.atendentes:
            if a.nome.lower() == nome_atendente.lower():
                atendente = a

        if atendente is None:
            print("Atendente não encontrado.")
            return

        utilizacao_encontrada.atendente_devolucao = atendente
        utilizacao_encontrada.aberta = False
        utilizacao_encontrada.toalha.disponivel = True

        print("Devolução realizada com sucesso.")