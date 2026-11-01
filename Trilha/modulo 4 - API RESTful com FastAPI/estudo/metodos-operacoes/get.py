from fastapi import FastAPI
from fastapi.responses import RedirectResponse # para redirecionar para outro lugar

app = FastAPI(
    title="API Estudo",
    description="estudo do metodo GET",
    version="0.1",
)

@app.get("/", include_in_schema=False) # include_in_schema=False = nao aparece no /docs 
def root():
    return RedirectResponse(url="/docs") # redireciona para /docs

# GET - pedir ou listar recursos existentes
@app.get("/status")
def status():
    return {
        "API Estudo": {"status":"active", "mensagem":"acesse /docs"}
    }

produtos = [
    {"id" : 1, "nome" : "livro"},
    {"id" : 2, "nome" : "celular"},
    {"id" : 3, "nome" : "notebook"},
    {"id" : 4, "nome" : "notes"}
]

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.get("/produtos/{id}")  # id é passado entre {} pq se trata de um produto unico e especifico e as chaves diz que se trata da ultima parte da URL
#teste -    curl http://127.0.0.1:8000/produtos/1
def listar_produto_por_id(id: int):
    produto = [p for p in produtos if p["id"] == id] # verifica se o id passado corresponde com == . verifica se é exetamente igual
    if produto:
        return produto
    return {"erro":"produto nao encontrado"}

@app.get("/produtos/buscar/") # O nome fica Query Parameter pois nao esta sendo passado diretamente na url, mas sim como um parametro de consulta, depois do ? 
# teste -   curl http://127.0.0.1:8000/produtos/buscar/?nome=a
def buscar_produto_por_nome(nome: str):
    produto = [p for p in produtos if nome.lower() in p["nome"].lower()]
    if produto:
        return produto
    else:
        return {"erro":"produto nao encontrado"}


