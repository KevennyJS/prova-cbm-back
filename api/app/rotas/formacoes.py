from fastapi import APIRouter, Body
from app.sql_app.database import connection
from app.models.formacoes import formacoes
from app.schemas.index import Formacao
from app.exemplos.index import exemplo_formacao
from fastapi.responses import JSONResponse

formacoes_rota = APIRouter()


@formacoes_rota.get("/formacoes")
async def read_data():
    return connection.execute("SELECT * FROM formacao").fetchall()


@formacoes_rota.post("/formacoes")
async def write_data(formacao: Formacao = Body(exemplo_formacao)):
    if formacao.instituicao_id == "" or formacao.perfil_id == "":
        return JSONResponse(status_code=404, content={"message": "Preencha todos os campos"})
    else:
        connection.execute(formacoes.insert().values(
            instituicao_id=formacao.instituicao_id,
            perfil_id=formacao.perfil_id,
            nome=formacao.nome
        ))
        return {'message': f"Formação cadastrada com sucesso"}
