# Expense Tracker API

Projeto MVP desenvolvido durante a Sprint 3 do curso de Pós-Graduação em Desenvolvimento Full Stack da PUC-Rio Digital, com o objetivo de explorar a implentação de Sistema composto por Front-End, BackEnd e consumo de API Externa.

A aplicação desenvolvida tem por objetivo fornecer uma aplicação que permita aos usuário realizarem o acompanhamento das suas despesas, receitas e categorizá-las.


### Desenho da solução
A API foi construída usando FastAPI e SQLModel para conexão com base de dados MySQL.



### Estrutura do projeto
```
expense-tracker-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── database
│   │   ├── __init__.py
│   │   └── engine.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── categories.py
│   │   ├── expenses.py
│   │   └── incomes.py
│   └── routers
│       ├── __init__.py
│       ├── categories.py
│       ├── expenses.py
│       └── incomes.py
├── requirements.txt
└── README.md
```


### Instalação

```
(env)$ pip install -r requirements.txt
```

### Como executar

```bash
(env)$ fastapi run
```
ou

```bash
(env)$ uvicorn app.main:app --reload
```

### Tecnologias
FastAPI
Pydantic
SQLModel
Mysql


### Como executar através do Docker


### TODO
Incluir  as funcionalidades principais
tecnologias utilizadas no desenvolvimento
explicar brevemente a estrutura de pastas e responsabilidades
Incluir informações sobre objetivo do projeto 
Desenho de arquitetura 
Dockercompose
Incluir link para documentação

![alt text](image.png)



