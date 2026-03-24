from pydantic import BaseModel

class ClienteIn(BaseModel):

    nome : str
    cpf : str