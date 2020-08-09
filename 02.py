import sqlite3
conexao = sqlite3.connect('livraria.db')
cur = conexao.cursor()


def qtd_registros():
    sql = "select * from tb_cliente"
    cur.execute(sql)
    registros = cur.fetchall()
    print(registros)
    qtd = len(registros)
    return qtd


#inserir - create
sql = "insert into tb_cliente values (122, 'Paula', 21)"

cur.execute(sql)
conexao.commit()
print('One record added succesfully')
print('qtd_registros= ', qtd_registros()) #chamada na função
cur.close()
conexao.close()
