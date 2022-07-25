from sqlalchemy import Table, Column, Integer, String
from app.sql_app.database import meta

instituicao = Table('instituicoes', meta,
                    Column('id', Integer, primary_key=True),
                    Column('nome', String(255)))
