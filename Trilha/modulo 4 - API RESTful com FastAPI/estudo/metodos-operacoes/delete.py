from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(
    title="API Estudo",
    description="estudo do metodo PUT e PATCH",
    version="0.4",
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


# DELETAR produto
@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int):
    global produtos
    produto = [p for p in produtos if p["id"] == produto_id]
    if not produto:
        return {"erro":"produto nao encontrado"}
    
    produtos = [p for p in produtos if p["id"] != produto_id]
    return {"mensagem": f"Produto {produto_id} deletado com sucesso"}