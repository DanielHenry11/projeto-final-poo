from typing import List
from modelos.nadador import Nadador
from modelos.atendente import Atendente
from modelos.toalha import Toalha
from modelos.utilizacao import Utilizacao

class NadoLivre:
    """Classe de aplicação responsável por manter os dados em memória."""

    def __init__(self) -> None:
        self.__nadadores: List[Nadador] = []
        self.__atendentes: List[Atendente] = []
        self.__toalhas: List[Toalha] = []
        self.__utilizacoes: List[Utilizacao] = []

    @property
    def nadadores(self) -> List[Nadador]:
        return self.__nadadores

    @property
    def atendentes(self) -> List[Atendente]:
        return self.__atendentes

    @property
    def toalhas(self) -> List[Toalha]:
        return self.__toalhas

    @property
    def utilizacoes(self) -> List[Utilizacao]:
        return self.__utilizacoes