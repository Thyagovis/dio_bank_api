from models.transacao import transacoes
from models.conta import contas
from database import database
from schemas.transacao import TransacaoIn

async def registrar_transacao(transacao : TransacaoIn):

    query = transacoes.insert().values(
        
        conta_id = transacao.conta_id,
        tipo_transacao = transacao.tipo_transacao,
        valor = transacao.valor
        
    )

    res = await database.execute(query)

    return res



async def realizar_transacao(transacao : TransacaoIn):

    valor = transacao.valor 
    valor_na_conta = await database.fetch_one(contas.select().where(contas.c.id == transacao.conta_id))
    valor_na_conta = valor_na_conta['saldo']

    if transacao.tipo_transacao.strip().lower() == 'saque':

        if valor > valor_na_conta:

            return "Saldo insuficiente"

        valor = -valor

    query_conta = contas.update().where(contas.c.id == transacao.conta_id).values(
        saldo = contas.c.saldo + valor
    )

    await database.execute(query_conta)
    res = await registrar_transacao(transacao)

    return {
        "id" : res,
        "tipo_transacao" : transacao.tipo_transacao,
        "valor" : transacao.valor
    }



async def read_all_transacoes():

    query = transacoes.select()
    
    return await database.fetch_all(query)



async def read_transacoes_by_id(id : int):

    query = transacoes.select().where(transacoes.c.conta_id == id)

    return await database.fetch_all(query)