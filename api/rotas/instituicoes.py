from fastapi import APIRouter
from sql_app import connection

instituicoes_rota = APIRouter()


@instituicoes_rota.get("/instituicoes")
async def read_data():
    return connection.execute("SELECT * FROM instituicoes").fetchall()
