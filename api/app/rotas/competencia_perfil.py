from fastapi import APIRouter, Body
from app.exemplos.index import exemplo_competencias_perfis
from app.schemas.competencia_perfil import Competencia_perfil
from app.sql_app.database import connection
from app.models.competencias_perfil import competencias_perfil
from fastapi.responses import JSONResponse

competencia_perfil_rota = APIRouter()


@competencia_perfil_rota.post("/competencias-perfis")
async def write_data(competencia_perfil: Competencia_perfil = Body(exemplo_competencias_perfis)):
    if competencia_perfil.competencia_id is None or competencia_perfil.perfil_id is None:
        return JSONResponse(status_code=404, content={"message": "Campo Invalido"})
    else:
        connection.execute(competencias_perfil.insert().values(
            competencia_id=competencia_perfil.competencia_id,
            perfil_id=competencia_perfil.perfil_id,
        ))
        return {'message': f"Competencia associada com sucesso"}
