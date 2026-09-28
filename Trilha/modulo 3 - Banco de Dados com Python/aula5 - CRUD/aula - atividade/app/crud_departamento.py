from sqlalchemy.orm import Session
from app.models import Departamento

def criar_departamento(db: Session, nome: str, sigla: str):
    existe = db.query(Departamento).filter(
        Departamento.sigla == sigla 
    ).first()
    
    if existe:
        raise ValueError(f"Sigla {sigla} já cadastrada")
        
    novo = Departamento(nome=nome, sigla=sigla)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_departamentos(db: Session):
    return db.query(Departamento).order_by(Departamento.nome).all()


def buscar_departamento(db: Session, depto_id: int):
    return db.query(Departamento).filter(
        Departamento.id == depto_id
    ).first()


def atualizar_departamento(db: Session, depto_id: int, nome=None, sigla=None):
    depto = buscar_departamento(db, depto_id)
    
    if not depto:
        raise ValueError(f"Departamento {depto_id} não encontrado")

    if nome != None:
        depto.nome = nome
    if sigla != None:
        depto.sigla = sigla
    db.commit()
    db.refresh(depto)
    return depto

def desativar_departamento(db: Session, id: int):
    dep = buscar_departamento(db, id)

    if not dep:
        raise ValueError(f'Departamento {id} não encontrado!')
    if not dep.ativo:
        raise ValueError(f'Funcionario {id} já esta inativo!')

    dep.ativo = False
    db.commit()
    return dep