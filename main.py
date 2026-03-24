from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from database import database, metadata, engine

from models.cliente import clientes
from models.conta import contas
from models.transacao import transacoes

from controllers import cliente, conta, transacao



@asynccontextmanager
async def lifespan(app : FastAPI):

    metadata.create_all(engine)
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan= lifespan)

app.include_router(cliente.router)
app.include_router(conta.router)
app.include_router(transacao.router)
