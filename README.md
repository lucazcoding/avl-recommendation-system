# 🧭 Sistema de Recomendação Hierárquica de Produtos (SRHP)

## 📋 Informações Gerais do Projeto

- Nome: Sistema de Recomendação Hierárquica de Produtos (SRHP)
- Linguagem: Python 3.10+
- Framework: Flask
- Arquitetura: Modular, MVC simplificado + Core AVL

---

## 📂 Estrutura de Diretórios

```
AVLSRHP/
│
├── app/
│   ├── _init_.py
│   ├── main.py
│   ├── core/
│   │   ├── _init_.py
│   │   ├── categoria.py
│   │   └── arvore_avl.py
│   │
│   ├── services/
│   │   ├── _init_.py
│   │   └── recomendacao_service.py
│   │
│   ├── api/
│   │   ├── _init_.py
│   │   └── routes.py
│   │
│   ├── cli/
│   │   ├── _init_.py
│   │   └── interface_cli.py
│   │
│   ├── tests/
│   │   ├── _init_.py
│   │   ├── test_avl.py
│   │   ├── test_recomendacao.py
│   │   └── test_api.py
│   │
│   └── utils/
│       ├── _init_.py
│       ├── timer.py
│       └── logger.py
│
├── docs/
│   ├── relatorio_tecnico.md
│   └── arquitetura_sistema.png
│
├── requirements.txt
└── README.md
````
---

## 🚀 Como Executar o Projeto
 ````
### Instalação
git clone https://github.com/lucazcoding/avl-recommendation-system
cd avl-recommendation-system

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows

pip install -r requirements.txt
````

### Executar API
```
python -m app.main
# Acesse: http://localhost:5000
```

### Executar CLI
```
python -m app.cli.interface_cli
```
### Executar Testes
```
pytest app/tests/
```
