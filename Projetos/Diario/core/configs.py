from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()
USER = os.getenv("USER")
SENHA = os.getenv("PASSWORD")
PORTA = os.getenv("DOOR")
BANCO = os.getenv("NOME_BANCO")


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = F"mysql+aiomysql://{USER}:{SENHA}@{PORTA}/{BANCO}"
    DBBaseModel: ClassVar  = declarative_base()
    
    JWT_SECRET: str = 'LqoT1NS2Pqc7xOVNqhZI8azZw8faDpECUCrbh-Xdn_I' # JSON Web Tokens (JWTs).
    '''
    python -c "import secrets; print(secrets.token_urlsafe(32))" # Gerar token
    '''
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True # O case sensitive serve para distinguir entre letras maiúsculas e minúsculas, tratando-as como caracteres diferentes
        

settings : Settings = Settings()