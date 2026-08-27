import mysql.connector

# 1. Conexão
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="cadastro"
)

cursor = conexao.cursor()

# 2. CREATE TABLE (Cursos)
sql_criar_tabela = """
CREATE TABLE IF NOT EXISTS cursos (
    idcurso INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(30) NOT NULL UNIQUE,
    descricao TEXT,
    carga INT UNSIGNED,
    totaulas INT UNSIGNED,
    ano YEAR DEFAULT '2026'
) DEFAULT CHARSET = utf8mb4;
"""
cursor.execute(sql_criar_tabela)
print("1. Tabela 'cursos' criada!")

# 3. INSERT (Inserir dados)
sql_insert = """
INSERT INTO cursos (nome, descricao, carga, totaulas, ano) 
VALUES (%s, %s, %s, %s, %s)
"""
dados_cursos = [
    ('HTML5', 'Curso completo de HTML5 e CSS3', 40, 37, '2022'),
    ('Python', 'Lógica de programação com Python', 40, 30, '2023'),
    ('SQL', 'Banco de dados MySQL', 30, 15, '2024')
]

# executemany para inserir vários de uma vez
cursor.executemany(sql_insert, dados_cursos)
conexao.commit()  # Obrigatório para salvar INSERTS/UPDATES/DELETES!
print(f"2. {cursor.rowcount} cursos inseridos com sucesso!")

# 4. UPDATE (Atualizar carga do curso de Python)
sql_update = "UPDATE cursos SET carga = %s WHERE nome = %s"
cursor.execute(sql_update, (60, 'Python'))
conexao.commit()
print("3. Curso de Python atualizado para 60 horas!")

# 5. SELECT (Consultar e exibir os dados no console)
cursor.execute("SELECT idcurso, nome, carga, ano FROM cursos;")
resultados = cursor.fetchall()

print("\n--- RESULTADO NO BANCO ---")
for idcurso, nome, carga, ano in resultados:
    print(f"ID: {idcurso} | Curso: {nome:<10} | Carga: {carga}h | Ano: {ano}")

# 6. Fechar conexão
cursor.close()
conexao.close()