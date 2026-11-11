from sqlalchemy import Integer, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from persistencia.banco import Base

class Utilizacao(Base):
    __tablename__ = "utilizacoes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    
    nadador_id: Mapped[int] = mapped_column(ForeignKey("nadadores.id"), nullable=False)
    toalha_id: Mapped[int] = mapped_column(ForeignKey("toalhas.id"), nullable=False)
    atendente_entrega_id: Mapped[int] = mapped_column(ForeignKey("atendentes.id"), nullable=False)
    atendente_devolucao_id: Mapped[int | None] = mapped_column(ForeignKey("atendentes.id"), nullable=True)
    
    aberta: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    # Relacionamentos ORM
    nadador: Mapped["Nadador"] = relationship("Nadador")
    toalha: Mapped["Toalha"] = relationship("Toalha")
    atendente_entrega: Mapped["Atendente"] = relationship("Atendente", foreign_keys=[atendente_entrega_id])
    atendente_devolucao: Mapped["Atendente | None"] = relationship("Atendente", foreign_keys=[atendente_devolucao_id])

    def __init__(self, nadador, toalha, atendente_entrega):
        self.nadador = nadador
        self.toalha = toalha
        self.atendente_entrega = atendente_entrega
        self.atendente_devolucao = None
        self.aberta = True