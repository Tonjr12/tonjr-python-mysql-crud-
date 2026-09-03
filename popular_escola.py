import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="escola_db"
    )
    cursor = conexao.cursor()

    sql = "INSERT INTO alunos (nome, data_nascimento, mensalidade, situacao) VALUES (%s, %s, %s, %s)"

    # Dados dos alunos que você já tinha cadastrado
    alunos_iniciais = [
        ("Mariana Costa", "2003-09-20", 500.00, "ativo"),
        ("Isaac Vitali", "2008-05-10", 450.00, "ativo"),
        ("Lucas Silva", "2005-04-15", 450.00, "ativo"),
        ("Carollyne Vitali", "2012-02-22", 450.00, "ativo")
    ]

    cursor.executemany(sql, alunos_iniciais)
    conexao.commit()

    print(f"Sucesso! {cursor.rowcount} alunos foram inseridos e o banco está populado novamente.")

except mysql.connector.Error as erro:
    print(f"Erro ao popular o banco: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()