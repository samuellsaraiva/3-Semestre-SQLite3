#usando lista

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

sql = "insert into tb_cliente values(?, ?, ?)"

lista_cliente=[
    ('06719462180', 'Samuel', 21),
    ('123456789', 'Alguém', 99)
]

cur.executemany(sql, lista_cliente)
conexao.commit()
print('One record added succesfully')
print('Quantidade de registros: ', qtd_registros())

cur.close()
conexao.close()