from typing import Union
from fastapi import FastAPI
from routes.index import *

app = FastAPI()

app.include_router(perfis_rota, tags=["perfis"])
app.include_router(signos_rota, tags=["signos"])

# TODO: rotas
# /signos - GET                       => Pendente
# /tipo-sanguineos - GET              => Pendente
# /instituicoes - GET                 => Pendente
# /competencias - GET                 => Pendente
# /perfis - GET                       => OK!
# /perfis - POST                      => OK!
# /perfis - DELETE                    => OK!
# /perfis - PUT                       => OK!

# teste de integração
# docker
# docker-compose

# python -m uvicorn main:app --reload
