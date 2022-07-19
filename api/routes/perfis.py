from fastapi import APIRouter
from config.db import connection
from models.perfis import perfis
from schemas.index import Perfil

perfil_rota = APIRouter()

@perfil_rota.get("/")
async def read_data():
    return connection.execute("SELECT * FROM perfis").fetchall()


@perfil_rota.get("/{id}")
async def read_data(id: int):
    return connection.execute(perfis.select().where(perfis.c.id == id)).fetchall()


@perfil_rota.post("/")
async def write_data(perfil: Perfil):
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
    return connection.execute(perfis.select()).fetchall()


@perfil_rota.put("/{id}")
async def update_data(id: int, perfil: Perfil):
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
    return connection.execute(perfis.select()).fetchall()


@perfil_rota.delete("/{id}")
async def delete_data(id: int):
    connection.execute(perfis.delete().where(perfis.c.id == id))
    return connection.execute(perfis.select()).fetchall()
