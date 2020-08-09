import sqlite3
from sqlite3 import Error

def select_all():
    sql = "SELECT * from tb_livro"          # Consulta toda a tabela
    try:
        cur.execute(sql)
        registros = cur.fetchall()                      # registros é uma lista
        print('Consultando todos:')
        for registro in registros:                       # Mostra na vertical
            print(registro)
        print("Total de resistros: ", len(registros))
    except Error as e:
        print('Mensagem de erro do select_all:')
        print(e)
def insert_one():
    sql="insert into tb_livro(titulo, autor, preco, ano) values(?, ?, ?, ?)"
    # sql="insert into tb_livro(titulo, autor, preco, ano) values('Java', 'Deitel', 250.00, '2014-06-08' )"
    # sql="insert into tb_livro(titulo, preco, ano) values('Java', 250.00, '2014-06-08' )" # Insert sem a coluna autor
    v_titulo = input("Título: ")
    v_nome = input("Nome: ")
    v_preco = float(input("Preço: "))
    v_ano = input('Ano [aaaa-mm-dd]: ')
    try:
        cur.execute(sql, (v_titulo, v_nome, v_preco, v_ano))
        conexao.commit()                                #Persistir os dados
        print ("one record added successfully")
    except Error as e:
        print('Mensagem de erro no insert_one:')
        print(e)
        conexao.rollback()
if __name__ == '__main__':               #main <tab>
    database = 'livros.db'
    conexao=sqlite3.connect(database)    #Criando a base de dados livros.db
    try:
        cur =conexao.cursor()                       # AttributeError: 'sqlite3.Cursor' object has no attribute 'eecute'
        cur.execute('''create table if not exists tb_livro(
            pk_idt  integer primary key autoincrement,  
            titulo   text unique, 
            autor   text not null,
            preco   float,
            ano      text)
            ''')
        conexao.commit()
    except Error as e:
        print('Mensagem de erro no main:')
        print(e)
        conexao.rollback()
        cur.close()
        conexao.close()
        exit(0)
    while True:
        opcao = int(input("[1] insert one\n[2] select all\n[6] drop table\n[0] sair\nOpção: "))
        if opcao == 1:
            insert_one()
        elif opcao ==2:
            select_all()
        elif opcao == 6:
            cur.execute('drop table tb_livro')
            break
        else:
            break
    cur.close()
    conexao.close()
"""
- insert_one, retirar autor
- constraint unique
- insert_one, digitar
"""