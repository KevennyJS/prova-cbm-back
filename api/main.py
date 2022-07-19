from typing import Union
from fastapi import FastAPI
from routes.index import perfil_rota

app = FastAPI()

app.include_router(perfil_rota)

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