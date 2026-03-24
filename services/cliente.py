from models.cliente import clientes
from database import database 
from schemas.cliente import ClienteIn
from view.cliente import ClienteOut



async def cadastrar_cliente(cliente : ClienteIn):

    cpf = cliente.cpf.strip()
    nome = cliente.nome.strip().lower()


    if len(cpf.replace("-", '').replace(".", '')) != 11:

        return "cpf invalido"
    
    if cpf[3] != "." or cpf[7] != '.' or cpf[11] != '-':

        return "cpf invalido"
    

    query_cliente = clientes.insert().values(
        cpf = cliente.cpf,
        nome = cliente.nome
    )

    id = await database.execute(query_cliente)

    return {
        "id" : id,
        "nome": cliente.nome
    }



async def remover_cliente(cliente_id : int):

    res_id = await ler_cliente_id(cliente_id)

    if res_id == None:

        return res_id

    query = clientes.delete().where(clientes.c.id == cliente_id)
    res_del = await database.execute(query)

    return res_del


async def ler_todos_clientes():
    
    query = clientes.select()
    response = await database.fetch_all(query)

    if response == []:

        return response

    return response



async def ler_cliente_id(cliente_id : int):

    query = clientes.select().where(clientes.c.id == cliente_id)
    res_cliente = await database.fetch_one(query)

    if res_cliente == None:

        return res_cliente
    
    return res_cliente