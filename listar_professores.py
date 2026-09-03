import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="escola_db"
    )
    cursor = conexao.cursor()

    print("\n=== LISTA DE PROFESSORES CADASTRADOS ===")
    cursor.execute("SELECT idprofessor, nome, especialidade, admissao FROM professores")

    professores = cursor.fetchall()

    for prof in professores:
        print(f"ID: {prof[0]} | Nome: {prof[1]:<16} | Especialidade: {prof[2]:<16} | Admissão: {prof[3]}")

except mysql.connector.Error as erro:
    print(f"Erro no banco de dados: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("\nConexão encerrada com sucesso.")
