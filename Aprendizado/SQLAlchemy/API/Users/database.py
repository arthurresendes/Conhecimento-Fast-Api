from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


engine = create_engine("sqlite:///users.db")
Base = declarative_base()
Sessao = sessionmaker(engine)

def get_db():
    db = Sessao()
    try:
        yield db
    finally:
        db.close()