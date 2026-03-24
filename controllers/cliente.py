from fastapi import APIRouter, status, HTTPException
from view.cliente import ClienteOut
from schemas.cliente import ClienteIn
from models.cliente import clientes
from database import database
from services.cliente import cadastrar_cliente, ler_todos_clientes, ler_cliente_id, remover_cliente

router = APIRouter(prefix= '/cliente')

@router.post('/add',status_code= status.HTTP_201_CREATED, response_model= ClienteOut)
async def create_cliente(cliente : ClienteIn) -> ClienteOut:

    res = await cadastrar_cliente(cliente)

    if res == "cpf invalido":

        raise HTTPException(
            status_code= 500,
            detail= "cpf invalido"
        )

    return res



@router.delete("/delete/{cliente_id}")
async def delete_cliente(cliente_id : int):

    res = await remover_cliente(cliente_id)

    if res == None:

        raise HTTPException(
            status_code= 404,
            detail= "cliente nao encontrado"
        )
    
    return res



@router.get("/{cliente_id}", response_model= ClienteOut)
async def read_cliente(cliente_id : int):

    res_cliente = await ler_cliente_id(cliente_id)

    if res_cliente == "cliente nao encontrado":

        raise HTTPException(
            status_code= 404,
            detail= "cliente nao encontrado"
        )

    return res_cliente



@router.get("/", response_model= list[ClienteOut])
async def read_clientes():

    res_clientes = await ler_todos_clientes()

    if res_clientes == []:

        raise HTTPException(
            status_code= 404,
            detail = "sem clientes cadastrados"
        )

    return res_clientes 