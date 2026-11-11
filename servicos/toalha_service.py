from typing import List
from sqlalchemy import select
from modelos.toalha import Toalha
from persistencia.banco import get_session

class ToalhaService:
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