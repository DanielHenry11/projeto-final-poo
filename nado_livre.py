from typing import List
from modelos.nadador import Nadador
from modelos.toalha import Toalha
from modelos.atendente import Atendente
from modelos.utilizacao import Utilizacao
from persistencia.nadador_persistencia import NadadorPersistencia
from persistencia.toalha_persistencia import ToalhaPersistencia
from persistencia.atendente_persistencia import AtendentePersistencia
from persistencia.utilizacao_persistencia import UtilizacaoPersistencia

class NadoLivre:
    def __init__(self) -> None:
        self.nadador_persistencia = NadadorPersistencia()
        self.toalha_persistencia = ToalhaPersistencia()
        self.atendente_persistencia = AtendentePersistencia()
        self.utilizacao_persistencia = UtilizacaoPersistencia()

        self._nadadores = []
        self._toalhas = []
        self._atendentes = []
        self._utilizacoes = []

        self.carregar_dados()

    def carregar_dados(self) -> None:
        self._nadadores = self.nadador_persistencia.carregar_todos()
        self._toalhas = self.toalha_persistencia.carregar_todas()
        self._atendentes = self.atendente_persistencia.carregar_todos()

        nadadores_map = {n.matricula: n for n in self._nadadores}
        toalhas_map = {t.codigo: t for t in self._toalhas}
        atendentes_map = {a.nome: a for a in self._atendentes}

        self._utilizacoes = self.utilizacao_persistencia.carregar_todas(
            nadadores_map, toalhas_map, atendentes_map
        )

    def salvar_dados(self) -> None:
        self.nadador_persistencia.salvar_todos(self._nadadores)
        self.toalha_persistencia.salvar_todas(self._toalhas)
        self.atendente_persistencia.salvar_todos(self._atendentes)
        self.utilizacao_persistencia.salvar_todas(self._utilizacoes)

    @property
    def nadadores(self) -> List[Nadador]:
        return self._nadadores

    @property
    def atendentes(self) -> List[Atendente]:
        return self._atendentes

    @property
    def toalhas(self) -> List[Toalha]:
        return self._toalhas

    @property
    def utilizacoes(self) -> List[Utilizacao]:
        return self._utilizacoes