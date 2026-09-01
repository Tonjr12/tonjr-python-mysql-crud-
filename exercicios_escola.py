# 1. Importa a biblioteca necessária para comunicar o Python com o servidor MySQL
import mysql.connector

try:
    # 2. Estabelece a conexão informando o endereço do servidor, usuário, senha e o banco alvo
    conexao = mysql.connector.connect(
        host="localhost",  # Servidor rodando na sua máquina local
        user="root",  # Usuário administrador do MySQL
        password="12345",  # A sua senha de acesso ao MySQL
        database="escola_db"  # Banco de dados específico onde os dados serão inseridos
    )

    # 3. Cria o objeto 'cursor', responsável por executar comandos SQL dentro da conexão
    cursor = conexao.cursor()

    # 4. Define o comando SQL usando placeholders (%s) para evitar ataques de SQL Injection
    # O uso do 'DEFAULT' no primeiro campo instrui o MySQL a gerar a chave primária (matricula) automaticamente
    sql = "INSERT INTO alunos VALUES (DEFAULT, %s, %s, %s, %s)"

    # 5. Lista contendo as tuplas com os dados dos alunos a serem inseridos
    # A ordem dos elementos obedece estritamente às colunas da tabela: (nome, data_nascimento, mensalidade, situacao)
    novos_alunos = [
        ("Lucas Silva", "2005-04-15", 450.00, "ativo"),
        ("Mariana Costa", "2003-09-20", 500.00, "ativo")
    ]

    # 6. O 'executemany' envia o comando SQL uma única vez aplicando toda a lista de alunos em lote
    cursor.executemany(sql, novos_alunos)

    # 7. O 'commit()' é obrigatório para confirmar e salvar definitivamente as alterações (DML) no banco de dados
    conexao.commit()

    # 8. Exibe uma mensagem de sucesso informando quantos registros foram inseridos no banco
    print(f"Sucesso! {cursor.rowcount} alunos cadastrados no banco 'escola_db'.")

except mysql.connector.Error as erro:
    # Captura e exibe eventuais erros de conexão ou de sintaxe SQL sem travar a execução
    print(f"Erro ao conectar ou inserir dados: {erro}")

finally:
    # 9. O bloco 'finally' sempre executa, garantindo o fechamento seguro dos recursos mesmo se ocorrer algum erro
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()  # Libera a memória do cursor
        conexao.close()  # Encerra a conexão ativa com o servidor MySQL
        print("Conexão encerrada com sucesso.")