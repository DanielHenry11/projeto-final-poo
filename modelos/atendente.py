from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from persistencia.banco import Base

class Atendente(Base):
    __tablename__ = "atendentes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)

    def __init__(self, nome: str):
        self.nome = nome