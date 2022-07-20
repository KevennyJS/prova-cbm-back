from pydantic import BaseModel


class BasicInfo(BaseModel):
    nome: str
