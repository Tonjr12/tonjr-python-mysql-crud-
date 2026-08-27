import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="cadastro"
    )
    cursor = conexao.cursor()

    # Seus comandos SQL aqui...

except mysql.connector.Error as erro:
    print(f"Erro no banco de dados: {erro}")
finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada com sucesso.")