from fastapi import APIRouter
from app.sql_app.database import connection

instituicoes_rota = APIRouter()


@instituicoes_rota.get("/instituicoes")
async def read_data():
    return connection.execute("SELECT * FROM instituicoes").fetchall()
