from typing import List
from sqlalchemy import select
from modelos.utilizacao import Utilizacao
from modelos.nadador import Nadador
from modelos.toalha import Toalha
from modelos.atendente import Atendente
from excecoes.nado_livre_error import ItemNaoEncontradoError, ToalhaIndisponivelError
from persistencia.banco import get_session

class UtilizacaoService:
    def __init__(self, app=None) -> None:
        self.__app = app

    def retirar(self, matricula: str, codigo: str, nome_atendente: str) -> Utilizacao:
        with get_session() as session:
            nadador = session.scalars(select(Nadador).where(Nadador.matricula == matricula)).first()
            if not nadador:
                raise ItemNaoEncontradoError("Nadador não encontrado.")

            toalha = session.scalars(select(Toalha).where(Toalha.codigo == codigo)).first()
            if not toalha:
                raise ItemNaoEncontradoError("Toalha não encontrada.")

            if not toalha.disponivel:
                raise ToalhaIndisponivelError("Esta toalha está em uso.")

            atendentes = session.scalars(select(Atendente)).all()
            atendente = next((a for a in atendentes if a.nome.lower() == nome_atendente.lower()), None)
            if not atendente:
                raise ItemNaoEncontradoError("Atendente não encontrado.")

            toalha.disponivel = False
            utilizacao = Utilizacao(nadador=nadador, toalha=toalha, atendente_entrega=atendente)
            
            session.add(utilizacao)
            session.commit()
            session.refresh(utilizacao)
            return utilizacao

    def devolver(self, codigo: str, nome_atendente: str) -> None:
        with get_session() as session:
            utilizacoes = session.scalars(select(Utilizacao).where(Utilizacao.aberta == True)).all()
            utilizacao = next((u for u in utilizacoes if u.toalha.codigo == codigo), None)
            
            if not utilizacao:
                raise ItemNaoEncontradoError("Utilização aberta não encontrada.")

            atendentes = session.scalars(select(Atendente)).all()
            atendente = next((a for a in atendentes if a.nome.lower() == nome_atendente.lower()), None)
            if not atendente:
                raise ItemNaoEncontradoError("Atendente não encontrado.")

            utilizacao.atendente_devolucao = atendente
            utilizacao.aberta = False
            utilizacao.toalha.disponivel = True

            session.commit()

    def listar_abertas(self) -> List[Utilizacao]:
        with get_session() as session:
            return list(session.scalars(select(Utilizacao).where(Utilizacao.aberta == True)).all())

    def listar_todas(self) -> List[Utilizacao]:
        with get_session() as session:
            return list(session.scalars(select(Utilizacao)).all())