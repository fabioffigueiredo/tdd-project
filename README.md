# API de Produtos - TDD Project

API REST para gerenciamento de produtos desenvolvida com FastAPI e MongoDB, seguindo as práticas de Test-Driven Development (TDD).

## 🚀 Funcionalidades

### CRUD Completo
- ✅ **Create**: Criação de produtos com tratamento de exceções
- ✅ **Read**: Busca por ID e listagem com filtros de preço
- ✅ **Update**: Atualização com verificação de existência e `updated_at` automático
- ✅ **Delete**: Remoção de produtos

### Funcionalidades Avançadas
- 🔍 **Filtros de Preço**: Busca por faixa de preços (`min_price` e `max_price`)
- ⚠️ **Tratamento de Exceções**: Mensagens de erro amigáveis
- 🕒 **Timestamps Automáticos**: `created_at` e `updated_at` gerenciados automaticamente
- 🧪 **Cobertura de Testes**: 100% dos endpoints testados

## 📋 Pré-requisitos

- Python 3.11+
- Poetry
- MongoDB
- Make (opcional)

## 🛠️ Instalação e Execução

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd tdd-project

# Instale as dependências
poetry install

# Configure o MongoDB (certifique-se que está rodando na porta 27017)
# Ou ajuste a DATABASE_URL no arquivo .env

# Execute a aplicação
poetry run uvicorn store.main:app --reload

# Execute os testes
make test
# ou
poetry run pytest
```

## 📚 Endpoints da API

### Produtos

| Método | Endpoint | Descrição | Status Code |
|--------|----------|-----------|-------------|
| POST | `/products/` | Criar produto | 201 |
| GET | `/products/` | Listar produtos (com filtros) | 200 |
| GET | `/products/{id}` | Buscar produto por ID | 200/404 |
| PATCH | `/products/{id}` | Atualizar produto | 200/404 |
| DELETE | `/products/{id}` | Deletar produto | 204/404 |

### Filtros de Preço

```bash
# Buscar produtos com preço entre 5000 e 8000
GET /products/?min_price=5000&max_price=8000

# Buscar produtos com preço mínimo de 1000
GET /products/?min_price=1000

# Buscar produtos com preço máximo de 5000
GET /products/?max_price=5000
```

### Exemplo de Produto

```json
{
  "name": "Smartphone XYZ",
  "quantity": 10,
  "price": 1299.99,
  "status": true
}
```

## 🏗️ Estrutura do Projeto

```
tdd-project/
├── store/                    # Código principal da aplicação
│   ├── controllers/          # Controladores da API (rotas)
│   ├── core/                 # Configurações e exceções
│   ├── db/                   # Configuração do banco de dados
│   ├── models/               # Modelos de dados
│   ├── schemas/              # Schemas Pydantic
│   ├── usecases/             # Lógica de negócio
│   └── main.py               # Aplicação FastAPI
├── tests/                    # Testes automatizados
│   ├── controllers/          # Testes dos controladores
│   ├── schemas/              # Testes dos schemas
│   ├── usecases/             # Testes dos casos de uso
│   └── conftest.py           # Configurações dos testes
├── .env                      # Variáveis de ambiente
├── Makefile                  # Comandos automatizados
├── pyproject.toml            # Configuração do Poetry
└── README.md                 # Este arquivo
```

## 🧪 Testes

O projeto possui cobertura completa de testes:

```bash
# Executar todos os testes
make test

# Executar testes com coverage
poetry run pytest --cov=store

# Executar testes específicos
poetry run pytest tests/controllers/test_product.py
```

## 🔧 Configuração

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=mongodb://localhost:27017/store_db
```

### MongoDB

Certifique-se de que o MongoDB está rodando:

```bash
# Usando Docker
docker run -d -p 27017:27017 --name mongodb mongo:latest

# Ou instale localmente e inicie o serviço
mongod
```

## 📖 Documentação da API

Após iniciar a aplicação, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🚀 Deploy

Para deploy em produção, configure as variáveis de ambiente apropriadas e use:

```bash
poetry run uvicorn store.main:app --host 0.0.0.0 --port 8000
```


## 👥 Autores

- Desenvolvido seguindo práticas de TDD
- API REST com FastAPI e MongoDB
- Testes automatizados com pytest
