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

---

### Testes feitos via insomnia 

#### Registrar uma nova atividade física
<img width="1912" height="1030" alt="image" src="https://github.com/user-attachments/assets/5631bf7f-0f6b-4f72-9e34-5f1202711c69" />

#### Listar todas as atividades registradas
<img width="1912" height="1032" alt="image" src="https://github.com/user-attachments/assets/fd4bfc0d-0257-429f-84eb-c94e1d545eb6" />


#### Listar todas as atividades de um funcionário específico

<img width="1911" height="1023" alt="image" src="https://github.com/user-attachments/assets/7c19c1ba-29dc-44cc-a720-6ff541f8c332" />


