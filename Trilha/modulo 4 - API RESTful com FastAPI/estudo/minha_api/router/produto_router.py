# Router — Endpoints com Banco de Dados
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from models.produto import Produto
from schemas.produto_schema import ProdutoCreate, ProdutoPatch, ProdutoResponse

router = APIRouter(prefix="/produtos", tags=["Produtos"])

# ── GET /produtos ── Listar todos
@router.get("/", response_model=List[ProdutoResponse])
def listar_produtos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    produtos = db.query(Produto).filter(Produto.ativo == True).offset(skip).limit(limit).all()
    return produtos

# buscar produto especifico
@router.get("/{produto_id}", response_model=ProdutoResponse)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Produto com ID {produto_id} não encontrado!"
        )
    return produto

@router.post("/", response_model=ProdutoResponse, status_code=201)
def criar_produto(dados: ProdutoCreate, db: Session = Depends(get_db)):
    produto = Produto(**dados.model_dump())
    db.add(produto)
    db.commit()
    db.refresh(produto)
    return produto




# PUT
@router.put("/{produto_id}", response_model=ProdutoResponse, status_code=201)
def substituir_produto(produto_id: int, dados:ProdutoCreate, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    for campo, valor in dados.model_dump().items():
        setattr(produto, campo, valor)
    db.commit()
    db.refresh(produto)
    return produto


# ── PATCH
@router.patch('/{produto_id}', response_model=ProdutoResponse)
def atualizar_produto(produto_id: int, dados: ProdutoPatch, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail='Produto não encontrado')
    # Atualiza apenas os campos enviados (exclude_none ignora os None)
    for campo, valor in dados.model_dump(exclude_none=True).items():
        setattr(produto, campo, valor)
    db.commit()
    db.refresh(produto)
    return produto