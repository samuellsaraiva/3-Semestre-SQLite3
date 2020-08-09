#insert com input

import sqlite3
conexao = sqlite3.connect('livraria.db')
cur = conexao.cursor()


def qtd_registros():
    sql = "select * from tb_cliente"
    cur.execute(sql)
    registros = cur.fetchall()
    for registro in registros:
        print(registro)
    qtd = len(registros)
    return qtd


sql = "insert into tb_cliente values (?, ?, ?)"

cpf1= input('CPF: ')
nome1= input('Nome: ')
idade1= int(input('Idade: '))
cur.execute(sql,(cpf1, nome1, idade1))
conexao.commit()

print("One record added succesfully")
print("Quantidade de registros= ", qtd_registros())

cur.close()
conexao.close()