from typing import List
from nado_livre import NadoLivre
from modelos.utilizacao import Utilizacao
from excecoes.nado_livre_error import ItemNaoEncontradoError, ToalhaIndisponivelError

class UtilizacaoService:
    def __init__(self, app: NadoLivre) -> None:
        self._app = app

    def retirar(self, matricula: str, codigo: str, nome_atendente: str) -> Utilizacao:
        nadador = next((n for n in self._app.nadadores if n.matricula == matricula), None)
        if not nadador:
            raise ItemNaoEncontradoError("Nadador não encontrado.")

        toalha = next((t for t in self._app.toalhas if t.codigo == codigo), None)
        if not toalha:
            raise ItemNaoEncontradoError("Toalha não encontrada.")

        if not toalha.disponivel:
            raise ToalhaIndisponivelError("Esta toalha está em uso.")

        atendente = next((a for a in self._app.atendentes if a.nome.lower() == nome_atendente.lower()), None)
        if not atendente:
            raise ItemNaoEncontradoError("Atendente não encontrado.")

        toalha.disponivel = False
        utilizacao = Utilizacao(nadador, toalha, atendente)
        self._app.utilizacoes.append(utilizacao)
        return utilizacao

    def devolver(self, codigo: str, nome_atendente: str) -> None:
        utilizacao = next((u for u in self._app.utilizacoes if u.toalha.codigo == codigo and u.aberta), None)
        if not utilizacao:
            raise ItemNaoEncontradoError("Utilização aberta não encontrada.")

        atendente = next((a for a in self._app.atendentes if a.nome.lower() == nome_atendente.lower()), None)
        if not atendente:
            raise ItemNaoEncontradoError("Atendente não encontrado.")

        utilizacao.atendente_devolucao = atendente
        utilizacao.aberta = False
        utilizacao.toalha.disponivel = True

    def listar_abertas(self) -> List[Utilizacao]:
        return [u for u in self._app.utilizacoes if u.aberta]

    def listar_todas(self) -> List[Utilizacao]:
        return self._app.utilizacoes