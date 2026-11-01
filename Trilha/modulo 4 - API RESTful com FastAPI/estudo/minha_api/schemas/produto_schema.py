# Schemas Pydantic — Validação de Dados
from pydantic import BaseModel, Field, field_validator
from typing import Optional

# Schema de ENTRADA — o que o cliente envia no POST
class ProdutoCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100, description="nome do produto")
    descricao: Optional[str] = Field(None, max_length=500)
    preco: float = Field(..., gt=0, description="Preço deve ser maior que zero")
    estoque: int = Field(0, ge=0, description="Estoque não pode ser negativo")

    # Validação customizada

    @field_validator("nome")
    @classmethod
    def nome_nao_pode_ser_so_espaco(cls, v):
        if not v.strip():
            raise ValueError("Nome não pode ser só espaços")
        return v.strip()

# Schema de ATUALIZAÇÃO PARCIAL — PATCH (todos opcionais)
class ProdutoPatch(BaseModel):
    nome:       Optional[str] = Field(None, min_length=2, max_length=100)
    descricao:  Optional[str] = Field(None, max_length=500)
    preco:      Optional[float] = Field(None, gt=0)
    estoque:    Optional[int] = Field(None, ge=0)



# Schema de SAÍDA — o que a API retorna
class ProdutoResponse(BaseModel):

    id:             int
    nome:           str
    descricao:      Optional[str]
    preco:          float
    estoque:        int
    ativo:          bool

    class Config:
        from_attributes = True # permite converter SQLAlchemy → Pydantic


"""
... Campo obrigatório (Ellipsis)
gt=0 Greater than (maior que) 0
ge=0 Greater or equal (maior ou igual a) 0
min_length=2 Mínimo de 2 caracteres
max_length=100 Máximo de 100 caracteres
description=... Texto que aparece no Swagger
"""