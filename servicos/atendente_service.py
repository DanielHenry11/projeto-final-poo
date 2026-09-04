from typing import List
from nado_livre import NadoLivre
from modelos.atendente import Atendente

class AtendenteService:
    def __init__(self, app: NadoLivre) -> None:
        self.__app = app

    def cadastrar(self, nome: str) -> Atendente:
        atendente = Atendente(nome)
        self.__app.atendentes.append(atendente)
        return atendente

    def listar(self) -> List[Atendente]:
        return self.__app.atendentes