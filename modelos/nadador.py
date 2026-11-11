from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from persistencia.banco import Base

class Nadador(Base):
    __tablename__ = "nadadores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    matricula: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula