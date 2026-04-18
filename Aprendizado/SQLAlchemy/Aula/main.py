from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///dados.db')
Base = declarative_base()
Sessao = sessionmaker(engine)

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id: int = Column(Integer, autoincrement=True, primary_key=True)
    nome: str = Column(String(40), unique=True)


# Base.metadata.create_all(engine) Depois de criado pode comentar embora ele ignore

# sessao = Sessao()  Ficar sessao aberta 


with Sessao() as sessao:
    usuario = Usuario(nome="Jose")
    sessao.add(usuario)
    sessao.commit()
    sessao.close()



with Sessao() as sessao:
    usuario = sessao.query(Usuario).filter_by(id=1).first()
    # usuario = session.query(Usuario).all()
    # usuario = session.query(Usuario).order_by(Usuario.nome.desc()).all()
    print(usuario.nome)



with Sessao() as sessao:
    usuario = sessao.query(Usuario).filter_by(id=1).first()
    usuario.nome = "Josias"
    sessao.commit()
    sessao.close()


with Sessao() as sessao:
    usuario = sessao.query(Usuario).filter_by(id=1).first()
    sessao.delete(usuario)
    sessao.commit()
    sessao.close()

