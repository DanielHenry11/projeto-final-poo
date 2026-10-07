from typing import List
from nado_livre import NadoLivre
from modelos.nadador import Nadador

class NadadorService:
    def __init__(self, app: NadoLivre) -> None:
        self._app = app

    def cadastrar(self, nome: str, matricula: str) -> Nadador:
        nadador = Nadador(nome, matricula)
        self._app.nadadores.append(nadador)
        return nadador

    def listar(self) -> List[Nadador]:
        return self._app.nadadores