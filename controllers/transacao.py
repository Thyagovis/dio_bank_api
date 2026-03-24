from fastapi import APIRouter, HTTPException, status
from view.transacao import TransacaoOut
from schemas.transacao import TransacaoIn
from services.transacao import read_transacoes_by_id, realizar_transacao, read_all_transacoes

router = APIRouter(prefix= '/transacao')



@router.post('/add/', status_code= status.HTTP_201_CREATED, response_model= TransacaoOut)
async def create_transacao(transacao : TransacaoIn):
    
    res = await realizar_transacao(transacao)

    if res == "Saldo insuficiente":
 
        raise HTTPException(
            status_code=400,
            detail="Saldo insuficiente"
        )

    return res
    


@router.get("/", response_model= list[TransacaoOut])
async def read_transacoes():

    res = await read_all_transacoes()

    if res == []:
 
        raise HTTPException(
            status_code=400,
            detail="Sem registros ainda"
        )

    return res



@router.get("/{id}", response_model= list[TransacaoOut])
async def read_transacoes_id(id : int):

    res = await read_transacoes_by_id(id)

    if res == []:
 
        raise HTTPException(
            status_code=400,
            detail="Conta nao encontrada"
        )

    return res