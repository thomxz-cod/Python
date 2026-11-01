from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from pydantic import BaseModel # biblioteca mais usada hoje em dia para validação de dados e gerenciamento de configurações

app = FastAPI(
    title="API Estudo",
    description="estudo do metodo POST",
    version="0.2",
)

@app.get("/", include_in_schema=False) # include_in_schema=False = nao aparece no /docs 
def root():
    return RedirectResponse(url="/docs") # redireciona para /docs

produtos = []
proximo_id = 1


@app.get("/produtos")
def listar_produtos():
    return produtos


# MODELS

# Modelo Pydantic - define e valida dados de entrada
class ProdutoEntrada(BaseModel):
    nome: str
    preco: float
    estoque: int = 0


# POST

@app.post("/produtos", status_code=201) # 201 significa que foi criado com sucesso
def criar_produto(produto: ProdutoEntrada):
    global proximo_id

    if produto.preco <= 0:
        return {"erro": "preço deve ser maior que zero"}

    novo_produto = { # cria a variavel do novo produto antes de adicionar na lista de produtos
        "id" : proximo_id,
        "nome" : produto.nome,
        "preco" : produto.preco,
        "estoque" : produto.estoque,
    }
    produtos.append(novo_produto) # adiciona na lista de produtos
    proximo_id += 1 # adiciona mais um no proximo id

    return novo_produto

