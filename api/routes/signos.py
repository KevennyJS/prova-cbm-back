from fastapi import APIRouter
from config.db import connection
from models.signos import signos
from schemas.index import Signo

signos_rota = APIRouter()


@signos_rota.get("/signos/")
async def read_data():
    return connection.execute("SELECT * FROM signos").fetchall()
