import mysql.connector

#vou conectar agora
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="cadastro"
)
cursor = conexao.cursor()

# vou definir o comando e vou-me cadastrar
sql = "INSERT INTO pessoas (nome, nascimento) VALUES (%s, %s)"
dados = ("Tonjr","1984-03-12")

#execultando e salvaldo
cursor.execute(sql, dados)
conexao.commit()

#fechando
cursor.close()
conexao.close()
print('cadastro realizado com sucesso')