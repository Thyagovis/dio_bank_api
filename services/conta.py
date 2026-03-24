from models.conta import contas
from models.cliente import clientes
from database import database 
from view.conta import ContaOut
from schemas.conta  import ContaIn
from sqlalchemy import select



async def criar_conta(conta : ContaIn):

    query_id =  select(clientes.c.id)
    rows = await database.fetch_all(query_id)
    ids = [row["id"] for row in rows]    

    if conta.cliente_id not in ids:

        return "cliente nao registrado"
    
    query_conta = contas.insert().values(
        saldo = conta.saldo,
        cliente_id = conta.cliente_id
    )

    id = await database.execute(query_conta)

    return {
        "id" : id,
        "cliente_id" : conta.cliente_id,
        "saldo" : conta.saldo
    }



async def deletar_conta(id : int):

    query_conta = contas.select().where(contas.c.id == id)
    res = await database.fetch_one(query_conta)

    if res == None:

        return res

    query = contas.delete().where(contas.c.id == id)
    res = await database.execute(query)

    return res



async def ler_contas_cliente(id : int):

    query_id =  select(clientes.c.id)
    rows = await database.fetch_all(query_id)
    ids = [row["id"] for row in rows]

    if id not in ids:

        return "cliente nao registrado"
    
    query = contas.select().where(contas.c.cliente_id == id)
    res = await database.fetch_all(query)

    return res



async def ler_todas_contas():

    query = contas.select()
    res = await database.fetch_all(query)

    if res == []:

        return res
    
    return res