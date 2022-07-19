from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# TODO: rotas
# /signos - GET
# /tipo-sanguineos - GET
# /instituicoes - GET
# /competencias - GET
# /perfis - GET
# /perfis - POST
# /perfis - DELETE
# /perfis - PUT

# teste de integração
# docker
# docker-compose
