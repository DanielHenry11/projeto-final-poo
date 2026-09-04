from typing import List
from nado_livre import NadoLivre
from modelos.nadador import Nadador

class NadadorService:
    def __init__(self, app: NadoLivre) -> None:
        self.__app = app

    def cadastrar(self, nome: str, matricula: str) -> Nadador:
        nadador = Nadador(nome, matricula)
        self.__app.nadadores.append(nadador)
        return nadador

    def listar(self) -> List[Nadador]:
        return self.__app.nadadores