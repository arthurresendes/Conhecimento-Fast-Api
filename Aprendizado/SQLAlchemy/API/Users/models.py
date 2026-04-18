from database import Base
from sqlalchemy import Column, Integer, Float, String, Boolean

class Usuario(Base):
    __tablename__ = 'usuarios'
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    email: str = Column(String, unique=True)
    idade: int  = Column(Integer)
    salario: float = Column(Float)
    empregado: bool = Column(Boolean)

