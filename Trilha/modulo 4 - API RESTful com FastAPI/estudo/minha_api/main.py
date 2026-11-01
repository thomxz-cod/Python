from fastapi import FastAPI
from database.db import engine, Base
from router.produto_router import router as produto_router
from fastapi.responses import RedirectResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de produtos",
    description="Estrutura Profissional",
    version="0.5"
)

app.include_router(produto_router) # registrar routers

@app.get("/", include_in_schema=False)
def raiz():
    return RedirectResponse(url="/docs")

@app.get("/sobre")
def sobre():
    return {"API de Estudo": "rodando em /docs"}

@app.get("/turma")
def turma():
    return {"Desenvolvimento de Sistemas Vespestino": "Thomaz Erick"}




