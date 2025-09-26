# API de Registro de Atividades Físicas

API RESTful simples que permite o **registros** e **consultas** de atividades físicas realizadas por funcionários.

---

## Tecnologias

- Python 3.11+
- Flask
- SQLAlchemy
- MySQL
- Pytest (testes unitários)
- Loguru (logs)
- python-dotenv (variáveis de ambiente)

---
## Estrutura do projeto
```bash
📦 api-registro-atividade-fisica
├─ .gitignore              # Arquivo que define quais arquivos/pastas o Git deve ignorar
├─ README.md               # Documentação do projeto
├─ app                     # Pasta principal da aplicação
│  ├─ __init__.py          # Cria a app factory e configura a aplicação Flask
│  ├─ extensions.py        # Inicializa extensões como SQLAlchemy
│  ├─ models               # Contém os modelos do banco de dados
│  │  └─ atividade_model.py  # Define o modelo Atividade
│  ├─ repositories         # Camada de acesso a dados (CRUD)
│  │  └─ atividade_repository.py  # Funções para manipular dados de Atividade no banco
│  ├─ routes               # Define rotas da aplicação
│  │  └─ atividades_routes.py  # Blueprint de atividades (endpoints GET, POST, etc.)
│  └─ services             # Lógica de negócio
│     └─ atividade_service.py  # Validação de dados e chamada ao repository
├─ requirements.txt        # Dependências do projeto (pip install -r requirements.txt)
├─ run.py                  # Entrypoint da aplicação (inicia o servidor Flask)
├─ setup_db.py             # Script para criar/configurar o banco de dados
└─ tests                   # Testes automatizados da aplicação
   ├─ __init__.py          # Permite que a pasta seja reconhecida como pacote Python
   ├─ conftest.py          # Fixtures e configurações globais do pytest
   └─ test_atividades.py   # Testes unitários das rotas de atividades


```
---

## Rodar localmente

Clone o projeto:
```bash
  git clone https://github.com/VinnyPC/api-registro-atividade-fisica.git
```

Vá para o diretório do projeto:

```bash
  cd api-registro-atividade-fisica
```

Criar e ativar o ambiente virtual:

```bash
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  venv\Scripts\activate     # Windows
```

Instalar as dependências:

```bash
  pip install -r requirements.txt
```

Configurar variáveis de ambiente no arquivo (.env):

```bash
  DB_HOST=127.0.0.1
  DB_PORT=3306
  DB_USER=root
  DB_PASS=root
  DB_NAME=db_atividades
```

### Inicialização do Banco de Dados
Execute o script de setup para criar o banco e tabelas:

```bash
  python setup_db.py
```

### Rodando a API Localmente
Execute o script de setup para criar o banco e tabelas:

```bash
  python run.py
```
Por padrão, a API fica disponível em: http://127.0.0.1:5000


---
### Endpoints
| **Método** | **URL**                 | **Descrição**                    |
|------------|-------------------------|----------------------------------|
| POST       | /atividades/            | Criar nova ativide               |
| GET        | /atividades/            | Listar todas as atividades       |
| GET        | /atividades/<funcional> | Buscar atividades pela funcional |

---

### Testes feitos via insomnia 

#### Registrar uma nova atividade física
<img width="1906" height="1029" alt="image" src="https://github.com/user-attachments/assets/de813ad4-c46b-49d6-b27c-700463af6001" />


#### Listar todas as atividades registradas
<img width="1915" height="1032" alt="image" src="https://github.com/user-attachments/assets/e0f04576-2a82-4ca5-b527-03de88de2ef3" />



#### Listar todas as atividades de um funcionário específico

<img width="1913" height="1036" alt="image" src="https://github.com/user-attachments/assets/d83519cc-fb32-47f6-a0bf-b768e50e6d19" />



