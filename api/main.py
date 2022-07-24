import uvicorn
from fastapi import FastAPI

from rotas.competencia_perfil import competencia_perfil_rota
from rotas.index import *

app = FastAPI(title="CBMSE API")

app.include_router(perfis_rota, tags=["Perfis"])
app.include_router(signos_rota, tags=["Signos"])
app.include_router(tipos_sanguineos_rota, tags=["Tipos sanguineos"])
app.include_router(instituicoes_rota, tags=["Instituicoes"])
app.include_router(competencias_rota, tags=["Competencias"])
app.include_router(competencia_perfil_rota, tags=["Competencia Perfil"])

# TODO: rotas
# /signos - GET                                                             => OK!
# /tipo-sanguineos - GET                                                    => OK!
# /instituicoes - GET                                                       => OK!
# /competencias - GET                                                       => OK!
# /perfis - GET                                                             => OK!
# /perfis - POST                                                            => OK!
# /perfis - DELETE                                                          => OK!
# /perfis - PUT                                                             => OK!

# extra
# /associar-competencia - POST                                              => OK!
# Gerar Comando SQL para buscar dados de -
# experiência, competendia e formação, no get de perfil                     => Pendente


# CPF deve conter válidição e quando mandado com mascara deve ser retirada. => OK!
# Data de Nascimento não pode permitir pessoas menores de 18 anos           => OK!
# E-mail deve ter validação de tipo                                         => OK!
# Formação pode ser mais de uma                                             => Pendente
# Experiência pode ser mais de uma                                          => Pendente
# Competencia pode ser mais de uma                                          => Pendente
# Sobre é campo texto livre                                                 => OK!
# Todos os campos são obrigatórios !!!!!                                    => OK!

# teste de integração                                                       => Pendente
# docker                                                                    => Pendente
# docker-compose                                                            => Pendente

# migrations                                                                 => OK!

# python -m uvicorn main:app --reload
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)