import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345",
        database="cadastro"
    )
    cursor = conexao.cursor()

    # Query SQL parametrizada (%s) para evitar SQL Injection
    sql_insert = """
    INSERT INTO pessoas (id, nome, nascimento, sexo, peso, altura, nacionalidade) 
    VALUES (DEFAULT, %s, %s, %s, %s, %s, %s);
    """

    lista_pessoas = [
        ('Godofredo', '1984-01-02', 'M', 78.5, 1.83, 'Brasil'),
        ('Maria', '1999-12-30', 'F', 55.2, 1.65, 'Portugal'),
        ('Creusa', '1920-05-15', 'F', 50.0, 1.65, 'Brasil'),
        ('Adalgisa', '1930-11-02', 'F', 53.2, 1.75, 'Irlanda'),
        ('Cláudio', '1975-04-22', 'M', 99.0, 2.15, 'Brasil'),
        ('Pedro', '1999-12-03', 'M', 87.0, 2.00, 'Brasil'),
        ('Janaína', '1987-11-12', 'F', 75.4, 1.66, 'EUA')
    ]

    # Inserção múltipla
    cursor.executemany(sql_insert, lista_pessoas)
    conexao.commit()  # Confirma a gravação dos dados no MySQL!

    print(f"Sucesso! {cursor.rowcount} registros inseridos na tabela 'pessoas'.")

except mysql.connector.Error as erro:
    print(f"Erro no banco de dados: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada com sucesso.")