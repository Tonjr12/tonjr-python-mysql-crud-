# 🚀 tonjr-python-mysql-crud
> Repositório para armazenar scripts SQL e automações em Python desenvolvidos durante os estudos de Banco de Dados MySQL.

## 📌 Tecnologias Utilizadas
- **MySQL Server & Workbench**
- **Python 3** (`mysql-connector-python`)
- **Git & GitHub**

## 📁 Estrutura do Repositório
- `01_criando_banco.sql`: Scripts SQL com criação de bancos, tabelas, tipos de dados e *constraints*.
- `02_exercicios_fixacao.sql`: Exercícios práticos em SQL puro (`loja_db`, `garagem_db`, `escola_db`).
- `conectar.py`: Script para teste de conexão entre Python e MySQL.
- `exercicios_guanabara.py` / `exercicios_guanabara_2.py`: Automação das operações DDL e DML acompanhando o curso.
- `cadastrar_professor.py`: Script específico para inserção automatizada na tabela de professores.
- `exercicios_tonjr_1.py`: Exercício autoral de fixação praticando `INSERT INTO` e `commit()`.
- `exercicios_escola.py`: Script com manipulação completa no banco `escola_db` (`INSERT`, `SELECT` e `DELETE`).

## 🚀 Como Executar os Scripts Python
1. Certifique-se de ter o servidor MySQL rodando localmente.
2. Instale o conector oficial do MySQL para Python:
   ```bash
   pip install mysql-connector-python