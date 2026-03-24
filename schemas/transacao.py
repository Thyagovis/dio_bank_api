from pydantic import BaseModel

class TransacaoIn(BaseModel):

    conta_id : int
    tipo_transacao : str
    valor : float