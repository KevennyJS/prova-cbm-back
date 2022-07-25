from fastapi import APIRouter, Body
from app.sql_app.database import connection
from app.models.index import perfis, formacoes, experiencias
from app.schemas.index import Perfil
from app.exemplos.index import exemplo_add_perfil, exemplo_update_perfil
from fastapi.responses import JSONResponse
from app.validacoes.perfil import PerfilValidacao

perfis_rota = APIRouter()


@perfis_rota.get("/perfis")
async def read_data():
    return connection.execute("SELECT * FROM perfis").fetchall()


@perfis_rota.get("/perfis/{id}")
async def read_data(id: int):
    perfil_encontrado = connection.execute(perfis.select().where(perfis.c.id == id)).first()
    competencias = connection.execute(
        "SELECT * FROM competencias WHERE id IN (SELECT competencia_id FROM competencias_perfis WHERE perfil_id = {})".format(id)).fetchall()
    formacoes_perfil = connection.execute(formacoes.select().where(formacoes.c.id == id)).fetchall()
    experiencia_perfil = connection.execute(experiencias.select().where(experiencias.c.id == id)).fetchall()

    if perfil_encontrado:
        return {
            "perfil": perfil_encontrado,
            "competencias": competencias,
            "formacoes": formacoes_perfil,
            "experiencias": experiencia_perfil
        }
    return JSONResponse(status_code=404, content={"message": "Perfil não encontrado"})


@perfis_rota.post("/perfis")
async def write_data(perfil: Perfil = Body(exemplo_add_perfil)):
    retornoValidacao = PerfilValidacao(perfil).validar_perfil()
    if retornoValidacao != "":
        return JSONResponse(status_code=404, content={"message": retornoValidacao})
    else:
        connection.execute(perfis.insert().values(
            tipos_sanguineo_id=perfil.tipos_sanguineo_id,
            signo_id=perfil.signo_id,
            cpf=perfil.cpf,
            nome=perfil.nome,
            data_nascimento=perfil.data_nascimento,
            email=perfil.email,
            telefone=perfil.telefone,
            resumo=perfil.resumo
        ))
        return {'message': f"Perfil cadastrado com sucesso"}


@perfis_rota.put("/perfis/{id}")
async def update_data(id: int, perfil: Perfil = Body(exemplo_update_perfil)):
    connection.execute(perfis.update().values(
        tipos_sanguineo_id=perfil.tipos_sanguineo_id,
        signo_id=perfil.signo_id,
        cpf=perfil.cpf,
        nome=perfil.nome,
        data_nascimento=perfil.data_nascimento,
        email=perfil.email,
        telefone=perfil.telefone,
        resumo=perfil.resumo
    ).where(perfis.c.id == id))
    return {'message': "Perfil atualizado com sucesso"}


@perfis_rota.delete("/perfis/{id}")
async def delete_data(id: int):
    connection.execute(perfis.delete().where(perfis.c.id == id))
    return {'message': "Perfil deletado com sucesso"}
