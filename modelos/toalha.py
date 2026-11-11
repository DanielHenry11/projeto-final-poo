from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import Mapped, mapped_column
from persistencia.banco import Base

class Toalha(Base):
    __tablename__ = "toalhas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    codigo: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    disponivel: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    def __init__(self, codigo: str):
        self.codigo = codigo
        self.disponivel = True