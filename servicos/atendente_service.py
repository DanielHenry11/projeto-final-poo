from typing import List
from sqlalchemy import select
from modelos.atendente import Atendente
from persistencia.banco import get_session

class AtendenteService:
    def __init__(self, app=None) -> None:
        self.__app = app

    def cadastrar(self, nome: str) -> Atendente:
        atendente = Atendente(nome)
        with get_session() as session:
            session.add(atendente)
            session.commit()
            session.refresh(atendente)
        return atendente

    def listar(self) -> List[Atendente]:
        with get_session() as session:
            return list(session.scalars(select(Atendente)).all())