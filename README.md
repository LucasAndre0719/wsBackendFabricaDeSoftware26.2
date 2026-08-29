# 🎬 CineHub API

API REST desenvolvida em **Django + Django REST Framework** para gerenciamento de filmes, gêneros e avaliações de usuários, com integração a uma API externa de filmes (SWAPI).

---

## 🚀 Funcionalidades

- **Gêneros de filmes** — CRUD completo (GET, POST, PUT, PATCH, DELETE)
  - `/api/generos/`

- **Filmes** — CRUD completo
  - `/api/filmes/`
  - Validação de duração mínima

- **Avaliações** — CRUD para usuários autenticados
  - `/api/avaliacoes/`
  - Cada usuário pode visualizar e gerenciar suas próprias avaliações
  - Nota validada entre 0 e 10
  - Impede que o mesmo usuário avalie o mesmo filme mais de uma vez

- **Filmes externos**
  - `/api/filmes_externos/`
  - Consulta filmes da saga Star Wars através da SWAPI
  - Filtro opcional por título:
    - `/api/filmes_externos/?titulo=Hope`

- **Autenticação por Token**
  - `/api/login/`
  - Retorna um token para autenticar requisições protegidas

- **Documentação da API**
  - Swagger disponível em `/api/docs/`

- **Painel administrativo**
  - Django Admin disponível em `/admin/`

---

## 🛠️ Tecnologias

- Python
- Django 6.1
- Django REST Framework
- drf-spectacular
- Requests
- SQLite
- SWAPI

---

# 💻 Como rodar o projeto

## Pré-requisitos

Antes de começar, é necessário ter instalado:

- Python 3.10 ou superior
- Git

O projeto não utiliza Docker ou banco de dados externo.

---

## 1. Clonar o repositório

Abra o terminal e execute:

```bash
git clone https://github.com/LucasAndre0719/wsBackendFabricaDeSoftware26.2.git
```

Entre na pasta do projeto:

```bash
cd wsBackendFabricaDeSoftware26.2
```

---

## 2. Criar o ambiente virtual

### Windows

```bash
python -m venv venv
```

Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

Quando estiver ativado, o terminal deverá apresentar algo parecido com:

```text
(venv) PS C:\...\wsBackendFabricaDeSoftware26.2>
```

### Linux/Mac

```bash
python3 -m venv venv
```

Ative:

```bash
source venv/bin/activate
```

---

## 3. Instalar as dependências

Com a `venv` ativada:

```bash
pip install -r requirements.txt
```

Esse comando instala as bibliotecas Python necessárias para executar o projeto.

---

## 4. Criar o banco de dados

Execute:

```bash
python manage.py migrate
```

Esse comando cria as tabelas necessárias no banco SQLite.

---

## 5. Criar um superusuário

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

Informe:

- Nome de usuário
- E-mail
- Senha

Essa etapa é opcional para utilizar a API, mas necessária caso queira acessar o Django Admin.

---

## 6. Executar os testes

Para executar os testes automatizados:

```bash
python manage.py test
```

O resultado esperado será parecido com:

```text
Ran X tests

OK
```

---

## 7. Iniciar o servidor

Execute:

```bash
python manage.py runserver
```

O servidor será iniciado em:

```text
http://127.0.0.1:8000/
```

---

# 🌐 Acessando o projeto

### API

```text
http://127.0.0.1:8000/api/
```

### Swagger

```text
http://127.0.0.1:8000/api/docs/
```

### Django Admin

```text
http://127.0.0.1:8000/admin/
```

---

# 🔐 Autenticação

O projeto utiliza **Token Authentication** para proteger as operações de avaliações.

## 1. Obter um token

Faça uma requisição POST para:

```text
/api/login/
```

Exemplo:

```bash
curl -X POST http://127.0.0.1:8000/api/login/ \
  -d "username=SEU_USUARIO&password=SUA_SENHA"
```

A API retornará algo parecido com:

```json
{
    "token": "SEU_TOKEN"
}
```

## 2. Utilizar o token

Nas requisições protegidas, envie o token no header:

```text
Authorization: Token SEU_TOKEN
```

No Swagger, utilize o botão **Authorize** e informe:

```text
Token SEU_TOKEN
```

---

# 📌 Principais endpoints

| Método | Endpoint | Descrição | Autenticação |
|---|---|---|---|
| GET | `/api/generos/` | Listar gêneros | Não |
| POST | `/api/generos/` | Criar gênero | Não |
| PUT/PATCH | `/api/generos/{id}/` | Editar gênero | Não |
| DELETE | `/api/generos/{id}/` | Remover gênero | Não |
| GET | `/api/filmes/` | Listar filmes | Não |
| POST | `/api/filmes/` | Criar filme | Não |
| PUT/PATCH | `/api/filmes/{id}/` | Editar filme | Não |
| DELETE | `/api/filmes/{id}/` | Remover filme | Não |
| GET | `/api/avaliacoes/` | Listar avaliações do usuário | Sim |
| POST | `/api/avaliacoes/` | Criar avaliação | Sim |
| PUT/PATCH | `/api/avaliacoes/{id}/` | Editar avaliação | Sim |
| DELETE | `/api/avaliacoes/{id}/` | Remover avaliação | Sim |
| GET | `/api/filmes_externos/` | Buscar filmes na SWAPI | Não |
| POST | `/api/login/` | Obter token | Não |
| GET | `/api/docs/` | Documentação Swagger | Não |

---

# ⭐ Regras das avaliações

As avaliações possuem algumas validações:

- A nota deve estar entre **0 e 10**.
- O usuário precisa estar autenticado.
- O usuário só pode gerenciar suas próprias avaliações.
- Um usuário não pode avaliar o mesmo filme mais de uma vez.

---

# 🌌 API externa

O projeto utiliza a **SWAPI** para consultar informações de filmes da saga Star Wars.

Endpoint utilizado:

```text
https://www.swapi.tech/api/films/
```

Também existe um filtro opcional por título:

```text
/api/filmes_externos/?titulo=Hope
```

A aplicação possui tratamento para:

- Erros de conexão;
- Respostas HTTP inesperadas;
- Respostas JSON inválidas;
- Filme não encontrado pelo título.

---

# 🧪 Testes

Os testes podem ser executados através do comando:

```bash
python manage.py test
```

Os testes verificam funcionalidades como:

- Criação de filmes;
- Criação de avaliações;
- Validação para impedir avaliações duplicadas.

---

# 📁 Estrutura básica do projeto

```text
wsBackendFabricaDeSoftware26.2/
│
├── app/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   └── viewsets.py
│
├── projeto/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚠️ Observações

Este projeto foi desenvolvido para fins acadêmicos.

O projeto está configurado com:

```python
DEBUG = True
```

Essa configuração é adequada para desenvolvimento local, mas não deve ser utilizada em produção.

O banco de dados utilizado atualmente é **SQLite**, não sendo necessário instalar ou configurar um banco de dados externo.

O projeto não utiliza Docker.

---

# 👨‍💻 Autor

Lucas André

Projeto desenvolvido para a Fábrica de Software.
