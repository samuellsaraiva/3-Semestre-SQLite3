import sqlite3

database = 'livraria.db'

conexao = sqlite3.connect(database)

cur = conexao.cursor()


cur.execute('''create table if not exists tb_cliente(
               cpf text,
               nome text,
               idade integer)''')

conexao.commit()
cur.close()
conexao.close()