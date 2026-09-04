from typing import List
from nado_livre import NadoLivre
from modelos.toalha import Toalha

class ToalhaService:
    def __init__(self, app: NadoLivre) -> None:
        self.__app = app

    def cadastrar(self, codigo: str) -> Toalha:
        toalha = Toalha(codigo)
        self.__app.toalhas.append(toalha)
        return toalha

    def listar(self) -> List[Toalha]:
        return self.__app.toalhas

    def listar_disponiveis(self) -> List[Toalha]:
        return [t for t in self.__app.toalhas if t.disponivel]