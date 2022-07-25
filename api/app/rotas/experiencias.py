from fastapi import APIRouter, Body

from app.exemplos.index import exemplo_experiencia
from app.sql_app.database import connection
from app.models.experiencias import experiencias
from app.schemas.index import Experiencia
from fastapi.responses import JSONResponse

experiencias_rota = APIRouter()


@experiencias_rota.get("/experiencias")
async def read_data():
    return connection.execute("SELECT * FROM experiencias").fetchall()


@experiencias_rota.post("/experiencias")
async def write_data(experiencia: Experiencia = Body(exemplo_experiencia)):
    if experiencia.perfil_id == "" or experiencia.empresa == "" or experiencia.inicio == "" or experiencia.fim == "" or experiencia.atual_trabalho == "" or experiencia.cargo == "":
        return JSONResponse(status_code=404, content={"message": "Preencha todos os campos"})
    else:
        connection.execute(experiencias.insert().values(
            perfil_id=experiencia.perfil_id,
            empresa=experiencia.empresa,
            inicio=experiencia.inicio,
            fim=experiencia.fim,
            atual_trabalho=experiencia.atual_trabalho,
            cargo=experiencia.cargo
        ))
        return {'message': f"Experiencia cadastrada com sucesso"}
