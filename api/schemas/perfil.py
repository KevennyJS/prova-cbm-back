import datetime
from typing import Optional

from pydantic import BaseModel


class Perfil(BaseModel):
    id: Optional[int] = None
    tipos_sanguineo_id: int
    signo_id: int
    cpf: str
    nome: str
    data_nascimento: datetime.datetime
    email: str
    telefone: str
    resumo: str
