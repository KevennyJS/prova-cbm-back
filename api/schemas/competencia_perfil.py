from pydantic import BaseModel


class Competencia_perfil(BaseModel):
    competencia_id: int
    perfil_id: int
