from pydantic import BaseModel

class TransacaoOut(BaseModel):

    id : int
    tipo_transacao : str
    valor : float 