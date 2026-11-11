from typing import List
from sqlalchemy import select
from modelos.toalha import Toalha
from persistencia.banco import get_session

class ToalhaService:
 banco-de-dados
    def __init__(self, app=None) -> None:
        self.__app = app

    def cadastrar(self, codigo: str) -> Toalha:
        toalha = Toalha(codigo)
        with get_session() as session:
            session.add(toalha)
            session.commit()
            session.refresh(toalha)
        return toalha

    def listar(self) -> List[Toalha]:
        with get_session() as session:
            return list(session.scalars(select(Toalha)).all())

    def listar_disponiveis(self) -> List[Toalha]:
        with get_session() as session:
            return list(session.scalars(select(Toalha).where(Toalha.disponivel == True)).all())

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
 main
