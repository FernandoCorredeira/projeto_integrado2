from conn import *


def create_categoria(data_name_categoria):
    cursor = mydb.cursor()
    query = f"INSERT INTO Categorias(nome) VALUES ('{data_name_categoria}')"
    cursor.execute(query)
    mydb.commit()

def create_product(data_user, data_name, data_invoice, data_categories, data_deposits, data_amount, data_value):
    cursor = mydb.cursor()
    query = f"INSERT INTO Produtos(id_categoria, id_deposito, id_usuario, nome_produto, quantidade_produto, preco_produto, nf_produto) VALUES ('{data_categories}','{data_deposits}','{data_user}', '{data_name}', '{data_amount}','{data_value}','{data_invoice}' )"
    cursor.execute(query)
    mydb.commit()
    mydb.close()

def get_usuarios():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM Usuarios')
    result = cursor.fetchall()
       
    return result


#TELA USUARIO/GERENTE
def get_solicitacao():
    cursor = mydb.cursor()
    query='SELECT id_usuario, id_solicitacao, nome_solicitacao, quantidade_solicitacao, preco_solicitacao FROM Solicitacoes WHERE EXISTS (SELECT * FROM Solicitacoes WHERE id_solicitacao = 1)'
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def create_solicitacao(data_user, data_name, data_categories, data_deposits, data_amount, data_value):
    cursor = mydb.cursor()
    query = f"INSERT INTO Solicitacoes(id_categoria, id_deposito, id_usuario, nome_solicitacao, quantidade_solicitacao, preco_solicitacao) VALUES ('{data_categories}','{data_deposits}','{data_user}', '{data_name}', '{data_amount}','{data_value}')"
    cursor.execute(query)
    mydb.commit()
    mydb.close()





