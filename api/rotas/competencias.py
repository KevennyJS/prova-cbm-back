from fastapi import APIRouter
from sql_app import connection

competencias_rota = APIRouter()


@competencias_rota.get("/competencias")
async def read_data():
    return connection.execute("SELECT * FROM competencias").fetchall()