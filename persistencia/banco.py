import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Cria a pasta dados caso não exista
os.makedirs("dados", exist_ok=True)

DB_URL = "sqlite:///dados/nado_livre.db"

engine = create_engine(DB_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_session():
    return SessionLocal()

def inicializar_banco():
    Base.metadata.create_all(bind=engine)