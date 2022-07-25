from fastapi import APIRouter
from app.sql_app.database import connection

signos_rota = APIRouter()


@signos_rota.get("/signos")
async def read_data():
    return connection.execute("SELECT * FROM signos").fetchall()


