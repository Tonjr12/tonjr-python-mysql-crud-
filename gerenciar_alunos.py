import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="escola_db"
    )
    cursor = conexao.cursor()

    # -------------------------------------------------------------
    # PASSO 1: MOSTRAR OS ALUNOS CADASTRADOS (SELECT)
    # -------------------------------------------------------------
    print("\n=== LISTA DE ALUNOS CADASTRADOS ===")
    cursor.execute("SELECT matricula, nome, mensalidade, situacao FROM alunos")


    # fetchall() puxa todas as linhas encontradas no banco
    alunos = cursor.fetchall()

    for aluno in alunos:
        print(f"ID: {aluno[0]} | Nome: {aluno[1]:<20} | Mensalidade: R${aluno[2]:.2f} | Status: {aluno[3]}")

    # -------------------------------------------------------------
    # PASSO 2: DELETAR UM ALUNO ESPECÍFICO (DELETE)
    # -------------------------------------------------------------
    # ATENÇÃO: Sempre use a cláusula WHERE apontando para a Chave Primária (ID)
    # para evitar apagar registros errados por engano!
    id_para_deletar = 1  # Coloque aqui o ID do aluno que deseja apagar

    sql_delete = "DELETE FROM alunos WHERE id = %s"
    cursor.execute(sql_delete, (id_para_deletar,))

    # Lembrou do commit? Para DELETE ele é obrigatório para salvar a remoção!
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"\n✅ Aluno com ID {id_para_deletar} removido com sucesso!")
    else:
        print(f"\n⚠️ Nenhum aluno encontrado com o ID {id_para_deletar}.")

    # -------------------------------------------------------------
    # PASSO 3: LISTAR NOVAMENTE PARA CONFIRMAR A REMOÇÃO
    # -------------------------------------------------------------
    print("\n=== LISTA ATUALIZADA ===")
    cursor.execute("SELECT id, nome, situacao FROM alunos")
    for aluno in cursor.fetchall():
        print(f"ID: {aluno[0]} | Nome: {aluno[1]}")

except mysql.connector.Error as erro:
    print(f"Erro no banco de dados: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("\nConexão encerrada com sucesso.")