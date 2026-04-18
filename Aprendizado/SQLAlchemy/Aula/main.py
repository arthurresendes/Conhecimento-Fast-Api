from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Relationship

engine = create_engine('sqlite:///dados.db')
Base = declarative_base()
Sessao = sessionmaker(engine)

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id: int = Column(Integer, autoincrement=True, primary_key=True)
    nome: str = Column(String(40), unique=True)

class Livro(Base):
    __tablename__ = 'livros'
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    nome = Column(String(200))
    ano = Column(Integer)
    autor_id = Column(Integer, ForeignKey('autores.id'))
    autor = Relationship('Autor', backref='livros', lazy='subquery')

class Autor(Base):
    __tablename__ = 'autores'
    
    id = Column(Integer, primary_key=True,autoincrement=True)
    nome = Column(String(200))
    idade = Column(Integer)

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


with Sessao() as sessao:
    livro = Livro(nome="Chapeuzinho Vermelho", ano=2026, autor_id=1)
    sessao.add(livro)
    sessao.commit()
    sessao.close()

with Sessao() as sessao:
    autor = sessao.query(Autor).filter_by(id=1).first()
    for livros in autor.livros:
        print(livros.nome)
