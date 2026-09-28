from sqlalchemy.orm import Session
from app.models import Funcionario

def criar_funcionario(db: Session, nome: str, email: str, telefone: str, salario: float):
    # verficar se o email ja existe
    existe = db.query(Funcionario).filter(
        Funcionario.email == email
    ).first()

    if existe:
        print(f'E-mail {email} já cadastrado!!')
        return None

    # criar Objeto
    novo = Funcionario(nome=nome, email=email, telefone=telefone, salario=salario)

    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_funcionarios(db: Session, ativos = True): # lista todos os funcionarios
    query = db.query(Funcionario)
    if ativos:
        query = query.filter(Funcionario.ativo == ativos)
        return query.order_by(Funcionario.nome).all()

def buscar_funcionario(db: Session, id: int): # lista funcionario buscado pelo id
    return db.query(Funcionario).filter(
        Funcionario.id == id
    ).first()

def atualizar_funcionario(db: Session, id: int, nome=None, telefone=None, salario=None):
    func = buscar_funcionario(db, id)

    if not func:
        raise ValueError(f'Funcionario {id} não encontrado!')

    if nome is not None:
        func.nome = nome
    if telefone is not None:
        func.telefone = telefone
    if salario is not None:
        func.salario = salario

    db.commit()
    db.refresh(func)
    return func

def desativar_funcionario(db: Session, id: int):
    func = buscar_funcionario(db, id)

    if not func:
        raise ValueError(f'Funcionario {id} não encontrado!')
    if not func.ativo:
        raise ValueError(f'Funcionario {id} já esta inativo!')

    func.ativo = False
    db.commit()
    return func