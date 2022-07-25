from pydantic import BaseModel
import datetime
from typing import Optional


class Experiencia(BaseModel):
    id: Optional[int] = None
    perfil_id: int
    empresa: str
    inicio: datetime.datetime
    fim: datetime.datetime
    atual_trabalho: int
    cargo: str
