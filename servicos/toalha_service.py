from typing import List
from nado_livre import NadoLivre
from modelos.toalha import Toalha

class ToalhaService:
    def __init__(self, app: NadoLivre) -> None:
        self._app = app

    def cadastrar(self, codigo: str) -> Toalha:
        toalha = Toalha(codigo)
        self._app.toalhas.append(toalha)
        return toalha

    def listar(self) -> List[Toalha]:
        return self._app.toalhas

    def listar_disponiveis(self) -> List[Toalha]:
        return [t for t in self._app.toalhas if t.disponivel]