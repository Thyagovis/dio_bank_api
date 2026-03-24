from fastapi import APIRouter, HTTPException, status
from view.conta import ContaOut
from schemas.conta import ContaIn
from models.conta import contas
from database import database
from services.conta import criar_conta, deletar_conta, ler_contas_cliente, ler_todas_contas

router = APIRouter(prefix= '/conta')



@router.post('/add/', status_code= status.HTTP_201_CREATED)
async def create_conta(conta : ContaIn):

    res = await criar_conta(conta)

    if res == "cliente nao registrado":

        raise HTTPException(
            status_code= 400,
            detail= "cliente nao registrado"
        )

    return res



@router.delete('/delete/{id}')
async def delete_conta(id : int):

    res = await deletar_conta(id)

    if res == None:

        raise HTTPException(
            status_code=404,
            detail= "Conta nao encontrada"
        )

    return res


@router.get('/cliente/{id}', response_model= list[ContaOut])
async def read_contas_cliente(id : int):

    res = await ler_contas_cliente(id)

    if res == "cliente nao registrado":

        raise HTTPException(
            status_code= 404,
            detail= "cliente nao registrado"
        )

    return res



@router.get('/', response_model= list[ContaOut])
async def read_todas_contas():

    res = await ler_todas_contas()

    if res == []:

        raise HTTPException(
            status_code= 404,
            detail= "sem clientes registrados"
        )

    return res