from pydantic import BaseModel

class ClienteOut(BaseModel):

    id : int
    nome : str