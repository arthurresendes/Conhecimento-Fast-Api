from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    nome: str
    email: str
    idade: int
    salario: float
    empregado: bool

class UserPatch(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    idade: Optional[int] = None
    salario: Optional[float] = None
    empregado: Optional[bool] = None