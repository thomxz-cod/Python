from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="API Estudo",
    description="estudo do metodo PUT e PATCH",
    version="0.3",
)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

produtos = [
    {"id" : 1, "nome" : "livro", "preco": 99.99, "estoque": 80},
    {"id" : 2, "nome" : "celular", "preco": 99.99, "estoque": 80},
    {"id" : 3, "nome" : "notebook", "preco": 99.99, "estoque": 80},
    {"id" : 4, "nome" : "notes", "preco": 99.99, "estoque": 80}
]

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/produtos/{id}")
def listar_produto_por_id(id: int):
    produto = [p for p in produtos if p["id"] == id]
    if produto:
        return produto
    return {"erro": "produto não encontrado"}



# MODELO PARA ATUALIZAR com PUT
class ProdutoAtualizacao_PUT(BaseModel):
    nome: str           # Obrigatorio
    preco: float        # Obrigatorio
    estoque: int        # Obrigatorio

# PUT - Atualiza todos os campos
@app.put("/produto/{produto_id}")
def alterar_produto_por_completo(produto_id: int, dados: ProdutoAtualizacao_PUT):
    for i, p in enumerate(produtos):
        if p["id"] == produto_id:
            produtos[i] = {
                "id" : produto_id,
                "nome" : dados.nome,
                "preco": dados.preco,
                "estoque": dados.estoque         
            }
            return produtos[i]
    return {"erro": "produto não encontrado!"}


# MODELO PARA ATUALIZAR com PATCH
class ProdutoAtualizacao_PATCH(BaseModel):
    nome: Optional[str]         # Obrigatorio
    preco: Optional[float]      # Obrigatorio
    estoque: Optional[int]      # Obrigatorio


# PATCH - atualiza apenas os campos que quiser
@app.patch("/produtos/{produto_id}")
def alterar_algum_campo_produto(produto_id: int, dados: ProdutoAtualizacao_PATCH):
    for p in produtos:
        if p["id"] == produto_id:
            if dados.nome is not None: p["nome"] = dados.nome
            if dados.preco is not None: p["preco"] = dados.preco
            if dados.estoque is not None: p["estoque"] = dados.estoque
        return p
    return {"erro": "produto não encontrado!"}