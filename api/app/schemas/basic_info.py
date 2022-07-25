from typing import Optional

from pydantic import BaseModel


class BasicInfo(BaseModel):
    id: Optional[int] = None
    nome: str
