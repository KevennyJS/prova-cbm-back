from fastapi import APIRouter, Body
from config.db import connection
from models.perfis import perfis
from schemas.index import Perfil
from exemplos.perfil import *
from fastapi.responses import JSONResponse
from validacoes.perfil import PerfilValidacao

perfis_rota = APIRouter()


@perfis_rota.get("/perfis")
async def read_data():
    return connection.execute("SELECT * FROM perfis").fetchall()


@perfis_rota.get("/perfis/{id}")
async def read_data(id: int):
    return connection.execute(perfis.select().where(perfis.c.id == id)).first()


@perfis_rota.post("/perfis")
async def write_data(perfil: Perfil = Body(exemplo_add_perfil)):
    retornoValidacao = PerfilValidacao(perfil).validar_perfil()
    if retornoValidacao != "":
        return JSONResponse(status_code=404, content={"message": retornoValidacao})
    else:
        retorno = connection.execute(perfis.insert().values(
            tipos_sanguineo_id=perfil.tipos_sanguineo_id,
            signo_id=perfil.signo_id,
            cpf=perfil.cpf,
            nome=perfil.nome,
            data_nascimento=perfil.data_nascimento,
            email=perfil.email,
            telefone=perfil.telefone,
            resumo=perfil.resumo
        ))
        return {'message': f"Perfil cadastrado com sucesso {retorno}"}


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
