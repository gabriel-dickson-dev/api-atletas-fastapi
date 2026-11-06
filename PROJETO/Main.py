from contextlib import asynccontextmanager
from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi_pagination import LimitOffsetPage, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Atleta
from schemas import AtletaCreate, AtletaOut


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Cria as tabelas na inicialização
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="API de Atletas", lifespan=lifespan)


@app.get("/atletas", response_model=LimitOffsetPage[AtletaOut])
def get_all_atletas(db: Session = Depends(get_db)):
    """Lista todos os atletas com paginação (?limit=10&offset=0)."""
    return paginate(db, select(Atleta).order_by(Atleta.id))


@app.get("/atletas/search", response_model=List[AtletaOut])
def get_atleta_by_nome_cpf(
    nome: Optional[str] = None,
    cpf: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """Busca atletas por nome (parcial, sem diferenciar maiúsculas) e/ou CPF."""
    query = db.query(Atleta)

    if nome:
        query = query.filter(Atleta.nome.ilike(f"%{nome}%"))
    if cpf:
        query = query.filter(Atleta.cpf == cpf)

    atletas = query.order_by(Atleta.id).all()

    if not atletas:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")

    return atletas


@app.post("/atletas", response_model=AtletaOut, status_code=status.HTTP_201_CREATED)
def create_atleta(payload: AtletaCreate, db: Session = Depends(get_db)):
    """Cadastra um novo atleta."""
    atleta = Atleta(**payload.model_dump())
    db.add(atleta)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Já existe um atleta cadastrado com o CPF {payload.cpf}",
        )
    db.refresh(atleta)
    return atleta


add_pagination(app)
