#consultar - read

import sqlite3
conexao = sqlite3.connect('livraria.db')
cur = conexao.cursor()

sql = "select * from tb_cliente"
cur.execute(sql)
registros = cur.fetchall()
print(type(registros))

if len(registros) > 0:
    print('Consultando todos.')
    for registro in registros:
        print(f'|| CPF: {registro[0]}, || Nome: {registro[1]}, || Idade: {registro[2]} ||\n')
        qtd = len(registros)
    print('Total de registros: ', qtd)

else:
    print('Lista vazia')

cur.close()
conexao.close()