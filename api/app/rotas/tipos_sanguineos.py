from fastapi import APIRouter
from app.sql_app.database import connection

tipos_sanguineos_rota = APIRouter()


@tipos_sanguineos_rota.get("/tipo-sanguineos/")
async def read_data():
    return connection.execute("SELECT * FROM tipos_sanguineos").fetchall()


