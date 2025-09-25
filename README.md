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
