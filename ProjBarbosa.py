import sqlite3
from sqlite3 import Error

database = 'corrida.db'

conexao = sqlite3.connect(database)

cur = conexao.cursor()

cur.execute('''create table if not exists tb_piloto(
                PK_Piloto integer primary key autoincrement,
                Nome_Piloto text,
                Idade integer,
                Categoria text
                FK_Pista integer)''')


def select_all_piloto():
    sql = "SELECT * from tb_piloto"
    try:
        cur.execute(sql)
        registros = cur.fetchall()
        for registro in registros:
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print(f'\nNumeração do Piloto: {registro[0]}\n'
                  f'Nome do Piloto: {registro[1]}\n'
                  f'Idade: {registro[2]}\n'
                  f'Categoria: {registro[3]}\n')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print(f'Total de registros: {len(registros)}')
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    except Error as erro_select_all:
        print(erro_select_all)


# sql = "insert into tb_piloto values(?, ?, ?)"
# lista_pilotos=[
#     ('Samuel', '21', Nascar),
#     ('Hériclys', '19', StockCar)
# ]
# cur.executemany(sql, lista_piloto)
# conexao.commit()


def insert_piloto():
    sql="insert into tb_piloto(Nome_Piloto, Idade, Categoria) values(?, ?, ?)"
    NomePiloto = input("Nome do Piloto: ")
    IdadePiloto = input("Idade do Piloto: ")
    CategoriaPiloto = input("Categoria a ser disputada: ")
    try:
        cur.execute(sql, (NomePiloto, IdadePiloto, CategoriaPiloto))
        conexao.commit()
    except Error as erro_insert:
        print(erro_insert)
        conexao.rollback()


def update_piloto():
    sql = "update tb_piloto set Nome_Piloto = ? where PK_Piloto = ?"
    try:
        NovoNomePiloto = input('Nome para atualizar:')
        PK_Piloto = input(('Nº Piloto: '))
        cur.execute(sql, (NovoNomePiloto, PK_Piloto))
        ct = cur.rowcount

        if ct > 0:
            print('Registro foi atualizado.')
        else:
            print('Nenhum registro foi atualizado.')
        conexao.commit()

    except Error as erro_update:
        print(erro_update)
        conexao.rollback()


def delete_piloto():
    sql = "delete from tb_piloto where PK_Piloto = ?"
    try:
        NumPiloto = input('Digite o nº do piloto para ser excluído: ')
        cur.execute(sql, (NumPiloto, ))
        ct = cur.rowcount

        if ct > 0:
            print('Registro foi apagado.')
        else:
            print('Nenhum registro foi apagado.')
        conexao.commit()

    except Error as erro_delete:
        print(erro_delete)
        conexao.rollback()


def select_piloto():
    sql = "select * from tb_piloto where PK_Piloto = ?"
    try:
        NumPiloto = input("Nº do piloto para seleção: ")
        cur.execute(sql, (NumPiloto, ))
        registro = cur.fetchone()

        if registro == None:
            print('Piloto não cadastrado.')
        else:
            print(registro)
            print(f'Numeração do Piloto: {registro[0]}\n,'
                  f'Nome do Piloto: {registro[1]}\n,'
                  f'Idade: {registro[2]}\n,'
                  f'Categoria: {registro[3]}\n\n')

    except Error as erro_select:
        print(erro_select)
        conexao.rollback()


cur.execute('''create table if not exists tb_pista(
                PK_Pista integer primary key autoincrement,
                Nome_Pista text,
                Voltas integer,
                Localizacao text)''')


def select_all_pista():
    sql = "SELECT * from tb_pista"
    try:
        cur.execute(sql)
        registros = cur.fetchall()
        for registro in registros:
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print(f'\nNumeração da Pista: {registro[0]}\n'
                  f'Nome da Pista: {registro[1]}\n'
                  f'Quantidade de Voltas desta pista: {registro[2]}\n'
                  f'Localização da Pista: {registro[3]}\n')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
        print("Total de registros: ", len(registros))
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    except Error as erro_all_pista:
        print(erro_all_pista)


def insert_pista():
    sql="insert into tb_pista(Nome_Pista, Voltas, Localizacao) values(?, ?, ?)"
    NomePista = input("Nome da Pista: ")
    VoltasPista = input("Quantidade de voltas: ")
    LocalizacaoPista = input("Localização da pista: ")
    try:
        cur.execute(sql, (NomePista, VoltasPista, LocalizacaoPista))
        conexao.commit()
    except Error as erro_insert:
        print(erro_insert)
        conexao.rollback()


def update_pista():
    sql = "update tb_pista set Nome_Pista = ? where PK_Pista = ?"
    try:
        NovoNomePista = input('Nome para atualizar:')
        PK_Pista = input(('Numeração da Pista: '))
        cur.execute(sql, (NovoNomePista, PK_Pista))
        ct = cur.rowcount

        if ct > 0:
            print('Registro atualizado.')
        else:
            print('Nenhum registro atualizado.')
        conexao.commit()

    except Error as erro_update:
        print(erro_update)
        conexao.rollback()


def delete_pista():
    sql = "delete from tb_pista where PK_Pista = ?"
    try:
        PK_Pista = input('Numeração da pista para ser retirada: ')
        cur.execute(sql, (PK_Pista, ))
        ct = cur.rowcount

        if ct > 0:
            print('Registro apagado.')
        else:
            print('Nenhum registro apagado.')
        conexao.commit()

    except Error as erro_delete:
        print(erro_delete)
        conexao.rollback()


def select_pista():
    sql = "select * from tb_pista where PK_Pista = ?"
    try:
        PK_Pista = input("Numeração da pista para selecionar: ")
        cur.execute(sql, (PK_Pista, ))
        registro = cur.fetchone()

        if registro == None:
            print('Pista não cadastrada.')
        else:
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
            print(f'\nNumeração da Pista: {registro[0]}\n'
                  f'Nome da Pista: {registro[1]}\n'
                  f'Quantidade de Voltas desta pista: {registro[2]}\n'
                  f'Localização da Pista: {registro[3]}\n')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    except Error as erro_select:
        print(erro_select)
        conexao.rollback()


if __name__ == '__main__':
    while True:
        print("Para manipular a tabela TB_Piloto, digite [1]")
        print("Para manipular a tabela TB_Pista, digite [2]")
        print("Para sair, digite [0]")

        op = int(input('\nDeseja manipular qual tabela? '))

        if op != 1 and op != 2 and op != 0:
            print('Opção inválida')
            break
        elif op == 0:
            print('Processo Finalizado!')
            break

        elif op == 1:
            while True:
                opcao = int(input("\n[1] Inserir algum dado na tabela\n"
                                  "[2] Selecionar todos os dados da tabela\n"
                                  "[3] Atualizar algum dado na tabela\n"
                                  "[4] Deletar algum dado da tabela\n"
                                  "[5] Selecionar algum dado da tabela\n"
                                  "[6] Apagar tabela\n"
                                  "[0] Sair das opções\n"
                                  "Opção: "))

                if opcao == 1:
                    insert_piloto()

                elif opcao == 2:
                    select_all_piloto()

                elif opcao == 3:
                    update_piloto()

                elif opcao == 4:
                    delete_piloto()

                elif opcao == 5:
                    select_piloto()

                elif opcao == 6:
                    cur.execute('drop table tb_piloto')
                    print("Tabela TB_Piloto apagada.\n")
                    break
                else:
                    print('Processo finalizado!')
                    break

        elif op == 2:
            while True:
                opcao = int(input("[1] Inserir algum dado na tabela\n"
                                  "[2] Selecionar todos os dados da tabela\n"
                                  "[3] Atualizar algum dado na tabela\n"
                                  "[4] Deletar algum dado da tabela\n"
                                  "[5] Selecionar algum dado da tabela\n"
                                  "[6] Apagar tabela\n"
                                  "[0] Sair das opções\n"
                                  "Opção: "))

                if opcao == 1:
                    insert_pista()

                elif opcao == 2:
                    select_all_pista()

                elif opcao == 3:
                    update_pista()

                elif opcao == 4:
                    delete_pista()

                elif opcao == 5:
                    select_pista()

                elif opcao == 6:
                    cur.execute('drop table tb_pista')
                    print("Tabela tb_pista apagada.\n")
                    break
                else:
                    print('Processo finalizado!\n')
                    break
        else:
            break

    cur.close()
    conexao.close()