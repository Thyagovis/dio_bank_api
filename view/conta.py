from pydantic import BaseModel

class ContaOut(BaseModel):

    id : int
    saldo : float
    cliente_id : int