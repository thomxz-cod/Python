Estrutura de projeto FastAPI profissional
minha-api/
│
├── main.py # Ponto de entrada — instancia o app e registra routers
├── config.py # Configurações (banco, variáveis de ambiente)
├── requirements.txt # Dependências do projeto
├── .env # Variáveis sensíveis (NÃO versionar no Git!)
├── .gitignore
│
├── models/ # Camada de dados (tabelas do banco)
│ ├── __init__.py
│ └── produto.py # Modelo SQLAlchemy da tabela produtos
│
├── schemas/ # Modelos Pydantic (validação de entrada/saída)
│ ├── __init__.py
│ └── produto_schema.py # ProdutoCreate, ProdutoResponse...
│
├── routers/ # Camada de controle (equivalente ao Controller)
│ ├── __init__.py
│ └── produto_router.py # Endpoints de produto
│
├── services/ # Regras de negócio complexas
│ ├── __init__.py
│ └── produto_service.py
│
└── database/ # Configuração do banco de dados
├── __init__.py
└── db.py





Autenticação JWT, Segurança e Documentação
```bash
pip install python-jose[cryptography] bcrypt python-multipart python-dotenv
```