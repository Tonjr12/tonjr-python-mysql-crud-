import mysql.connector

# 1. Conexão com o banco 'cadastro'
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="cadastro"
)

cursor = conexao.cursor()

# 2. CREATE TABLE
sql_criar_tabela = """
CREATE TABLE IF NOT EXISTS professores (
    idprofessor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    especialidade VARCHAR(50) DEFAULT 'Tecnologia',
    admissao DATE DEFAULT (CURRENT_DATE)
) DEFAULT CHARSET = utf8mb4;
"""
cursor.execute(sql_criar_tabela)

# 3. INSERT (Eduardo Castro especialista em Cybersecurity)
sql_inserir = """
INSERT INTO professores (nome, especialidade) 
VALUES (%s, %s);
"""
dados_professor = ("Eduardo Castro", "Cybersecurity")

cursor.execute(sql_inserir, dados_professor)
conexao.commit()
print(f"Professor {dados_professor[0]} ({dados_professor[1]}) cadastrado com sucesso!")

# 4. SELECT para conferir
cursor.execute("SELECT idprofessor, nome, especialidade, admissao FROM professores;")
professores = cursor.fetchall()

print("\n--- PROFESSORES NO BANCO ---")
for idprof, nome, espec, data_adm in professores:
    print(f"ID: {idprof} | Nome: {nome} | Especialidade: {espec} | Data: {data_adm}")

cursor.close()
conexao.close()