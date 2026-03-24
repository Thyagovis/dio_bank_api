from pydantic import BaseModel
from typing import Optional

class ContaIn(BaseModel):

    saldo : Optional[int] = 0
    cliente_id : int