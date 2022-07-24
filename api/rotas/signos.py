from fastapi import APIRouter
from sql_app import connection

signos_rota = APIRouter()


@signos_rota.get("/signos")
async def read_data():
    return connection.execute("SELECT * FROM signos").fetchall()


