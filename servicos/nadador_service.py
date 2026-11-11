from typing import List
from sqlalchemy import select
from modelos.nadador import Nadador
from persistencia.banco import get_session

class NadadorService:
 banco-de-dados
    def __init__(self, app=None) -> None:
        self.__app = app

    def cadastrar(self, nome: str, matricula: str) -> Nadador:
        nadador = Nadador(nome, matricula)
        with get_session() as session:
            session.add(nadador)
            session.commit()
            session.refresh(nadador)
        return nadador

    def listar(self) -> List[Nadador]:
        with get_session() as session:
            return list(session.scalars(select(Nadador)).all())

    def __init__(self, app: NadoLivre) -> None:
        self._app = app

    def cadastrar(self, nome: str, matricula: str) -> Nadador:
        nadador = Nadador(nome, matricula)
        self._app.nadadores.append(nadador)
        return nadador

    def listar(self) -> List[Nadador]:
        return self._app.nadadores
 main
