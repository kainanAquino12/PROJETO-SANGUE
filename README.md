# 🩸 Projeto Sangue API

API RESTful para gerenciamento de doadores de sangue, permitindo cadastro, consulta e filtragem de dados.

---

## 🚀 Sobre o projeto

Esta API foi desenvolvida utilizando **Python + Flask**, com o objetivo de simular um sistema simples de banco de sangue.

Permite:

* Cadastro de doadores
* Listagem de registros
* Busca por ID
* Filtro por idade
* Retorno de dados em JSON

---

## 📁 Estrutura do Projeto

```bash
PROJETO-SANGUE/
│
├── README.md          ← (documentação principal)
├── api.py             ← API Flask
├── doadores.json      ← Dados dos doadores
├── estoque.json       ← Dados do estoque
├── sangue.json        ← Dados das doações
│
├── docs/              ← (documentação extra)
│   └── projeto.md
│
└── assets/            ← (imagens)
    ├── busca-por-idade.png
    ├── resultado-json.png
    ├── busca-por-id.png
    ├── erro-404.png
    └── ...
```

---

## ⚙️ Como executar

### 1. Ativar ambiente virtual

```bash
venv\Scripts\activate
```

### 2. Instalar dependências

```bash
pip install flask
```

### 3. Executar a API

```bash
python api.py
```

---

## 🔎 Endpoints

### 📌 Listar doadores

```http
GET /doadores
```

### 📌 Filtrar por idade

```http
GET /doadores?idade=21
```

### 📌 Buscar por ID

```http
GET /doadores/<int:id>
```

---

## 🖼️ Exemplos

### 🔍 Busca por idade


![alt text](image-1.png)



### 🆔 Busca por ID


![alt text](image.png)


---

## 📦 Exemplo de resposta

```json
{
  "id": 1,
  "paciente": "Kainan",
  "idade": 21,
  "contato": "+55 45 9901-4255"
}
```

---

## 📄 Documentação completa

Acesse a documentação detalhada da API:

👉 [docs/projeto.md](docs/projeto.md)

---

## 🛠️ Tecnologias utilizadas

* Python
* Flask
* JSON

---

## 📌 Observações

* Projeto com fins educacionais
* Estrutura simples para aprendizado de APIs REST
* Pode ser expandido com banco de dados futuramente

---
