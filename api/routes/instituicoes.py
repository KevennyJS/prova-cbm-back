from fastapi import APIRouter
from config.db import connection

instituicoes_rota = APIRouter()


@instituicoes_rota.get("/instituicoes")
async def read_data():
    return connection.execute("SELECT * FROM instituicoes").fetchall()
