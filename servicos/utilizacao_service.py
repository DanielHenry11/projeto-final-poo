from typing import List
from sqlalchemy import select
from modelos.utilizacao import Utilizacao
from modelos.nadador import Nadador
from modelos.toalha import Toalha
from modelos.atendente import Atendente
from excecoes.nado_livre_error import ItemNaoEncontradoError, ToalhaIndisponivelError
from persistencia.banco import get_session

class UtilizacaoService:
 banco-de-dados
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

    def __init__(self, app: NadoLivre) -> None:
        self._app = app

    def retirar(self, matricula: str, codigo: str, nome_atendente: str) -> Utilizacao:
        nadador = next((n for n in self._app.nadadores if n.matricula == matricula), None)
        if not nadador:
            raise ItemNaoEncontradoError("Nadador não encontrado.")

        toalha = next((t for t in self._app.toalhas if t.codigo == codigo), None)
        if not toalha:
            raise ItemNaoEncontradoError("Toalha não encontrada.")
 main

            if not toalha.disponivel:
                raise ToalhaIndisponivelError("Esta toalha está em uso.")

 banco-de-dados
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

        atendente = next((a for a in self._app.atendentes if a.nome.lower() == nome_atendente.lower()), None)
        if not atendente:
            raise ItemNaoEncontradoError("Atendente não encontrado.")

        toalha.disponivel = False
        utilizacao = Utilizacao(nadador, toalha, atendente)
        self._app.utilizacoes.append(utilizacao)
        return utilizacao

    def devolver(self, codigo: str, nome_atendente: str) -> None:
        utilizacao = next((u for u in self._app.utilizacoes if u.toalha.codigo == codigo and u.aberta), None)
        if not utilizacao:
            raise ItemNaoEncontradoError("Utilização aberta não encontrada.")

        atendente = next((a for a in self._app.atendentes if a.nome.lower() == nome_atendente.lower()), None)
        if not atendente:
            raise ItemNaoEncontradoError("Atendente não encontrado.")
 main

            utilizacao.atendente_devolucao = atendente
            utilizacao.aberta = False
            utilizacao.toalha.disponivel = True

            session.commit()

    def listar_abertas(self) -> List[Utilizacao]:
 banco-de-dados
        with get_session() as session:
            return list(session.scalars(select(Utilizacao).where(Utilizacao.aberta == True)).all())

    def listar_todas(self) -> List[Utilizacao]:
        with get_session() as session:
            return list(session.scalars(select(Utilizacao)).all())

        return [u for u in self._app.utilizacoes if u.aberta]

    def listar_todas(self) -> List[Utilizacao]:
        return self._app.utilizacoes
 main
