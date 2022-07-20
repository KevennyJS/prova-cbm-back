import datetime
from pydantic import BaseModel


class Perfil(BaseModel):
    tipos_sanguineo_id: int
    signo_id: int
    cpf: str
    nome: str
    data_nascimento: datetime.datetime
    email: str
    telefone: str
    resumo: str
