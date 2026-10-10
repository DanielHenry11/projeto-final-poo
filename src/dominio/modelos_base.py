from abc import ABC, abstractmethod


class Usuario(ABC):
    """Classe abstrata base que representa um utilizador da escola de natação."""

    def __init__(self, id_usuario: int, nome: str) -> None:
        self._id_usuario = id_usuario
        self._nome = nome
        self._toalhas_empossadas: int = 0

    @property
    def id_usuario(self) -> int:
        """Retorna o ID do utilizador."""
        return self._id_usuario

    @property
    def nome(self) -> str:
        """Retorna o nome do utilizador."""
        return self._nome

    @property
    def toalhas_empossadas(self) -> int:
        """Retorna a quantidade de toalhas atualmente em posse do utilizador."""
        return self._toalhas_empossadas

    @abstractmethod
    def limite_maximo_toalhas(self) -> int:
        """Retorna o limite máximo de toalhas que o utilizador pode retirar simultaneamente."""
        pass

    def incrementar_toalhas(self) -> None:
        """Incrementa a contagem de toalhas em posse do utilizador."""
        self._toalhas_empossadas += 1

    def decrementar_toalhas(self) -> None:
        """Decrementa a contagem de toalhas em posse do utilizador."""
        if self._toalhas_empossadas > 0:
            self._toalhas_empossadas -= 1


class Aluno(Usuario):
    """Representa um aluno da escola de natação."""

    def limite_maximo_toalhas(self) -> int:
        # Regra de negócio: Alunos podem retirar no máximo 1 toalha por vez
        return 1


class Professor(Usuario):
    """Representa um professor da escola de natação."""

    def limite_maximo_toalhas(self) -> int:
        # Regra de negócio: Professores podem retirar até 3 toalhas por vez
        return 3


class Toalha:
    """Representa uma toalha pertencente ao acervo da escola."""

    def __init__(self, id_toalha: int, tamanho: str) -> None:
        self._id_toalha = id_toalha
        self._tamanho = tamanho
        self._disponivel: bool = True

    @property
    def id_toalha(self) -> int:
        """Retorna o ID da toalha."""
        return self._id_toalha

    @property
    def tamanho(self) -> str:
        """Retorna o tamanho da toalha (ex: P, M, G)."""
        return self._tamanho

    @property
    def disponivel(self) -> bool:
        """Indica se a toalha está disponível para empréstimo."""
        return self._disponivel

    @disponivel.setter
    def disponivel(self, status: bool) -> None:
        self._disponivel = status