from fastapi import FastAPI, status, Depends, HTTPException
from models import Usuario
from database import engine, Base,get_db
from sqlalchemy.orm import Session
import uvicorn
from typing import List
from schema import User,UserPatch

Base.metadata.create_all(engine)
app = FastAPI()

@app.get("/todos_users", status_code=status.HTTP_200_OK, tags=['Todos usuarios'], summary='Rota Get', response_model=List[User])
def ver_todos(db: Session = Depends(get_db)):
    usuario = db.query(Usuario).all()
    return usuario

@app.post("/cadastrar", status_code=status.HTTP_201_CREATED, tags=['Cadastrar Usuario'], summary='Rota Post')
def cadastro(user: User,db: Session = Depends(get_db)):
    usuario = Usuario(nome= user.nome, idade=user.idade, salario=user.salario, empregado=user.empregado, email=user.email)
    db.add(usuario)
    db.commit()

@app.delete("/deletar/{id}", status_code=status.HTTP_204_NO_CONTENT,tags=['Deletar Usuario'], summary='Rota Delete')
def deletar(id: int, db: Session = Depends(get_db)):
    user_delete = db.query(Usuario).filter(Usuario.id == id).first()
    db.delete(user_delete)
    db.commit()

@app.put("/atualizar/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['Atualizar todos os campos do Usuario'], summary='Rota Put', response_model=User)
def atualizar_todas_info(user: User, id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if usuario:
        usuario.nome = user.nome
        usuario.email = user.email
        usuario.salario = user.salario
        usuario.empregado = user.empregado
        usuario.idade = user.idade
        
        db.commit()
        return usuario
    else:
        raise HTTPException(detail="Usuario não encontrado", status_code=status.HTTP_404_NOT_FOUND)

@app.patch("/atualizar_alguns/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['Atualizar alguns campos do Usuario'], summary='Rota Patch', response_model=User)
def atualizar_especificos(user: UserPatch, id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if usuario:
        dados_atualizados = user.model_dump(exclude_unset=True)
        for campo, valor in dados_atualizados.items():
            setattr(usuario,campo,valor)
        db.commit()
        db.refresh(usuario)
        return usuario
    else:
        raise HTTPException(detail="Usuario não encontrado", status_code=status.HTTP_404_NOT_FOUND)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)