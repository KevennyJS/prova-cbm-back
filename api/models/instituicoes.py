from sqlalchemy import Table, Column, Integer, String
from config.db import meta

instituicao = Table('instituicoes', meta,
                    Column('id', Integer, primary_key=True),
                    Column('nome', String))
