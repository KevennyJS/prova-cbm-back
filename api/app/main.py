from fastapi import FastAPI

from app.rotas.index import *

app = FastAPI(title="CBMSE API")

app.include_router(perfis_rota, tags=["Perfis"])
app.include_router(signos_rota, tags=["Signos"])
app.include_router(tipos_sanguineos_rota, tags=["Tipos sanguineos"])
app.include_router(instituicoes_rota, tags=["Instituicoes"])
app.include_router(competencias_rota, tags=["Competencias"])
app.include_router(competencia_perfil_rota, tags=["Competencia Perfil"])
app.include_router(formacoes_rota, tags=["Formações"])
app.include_router(experiencias_rota, tags=["Experiencias"])
