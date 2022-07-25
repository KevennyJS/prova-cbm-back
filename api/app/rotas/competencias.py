from fastapi import APIRouter
from app.sql_app.database import connection

competencias_rota = APIRouter()


@competencias_rota.get("/competencias")
async def read_data():
    return connection.execute("SELECT * FROM competencias").fetchall()