from sqlalchemy import Table, Column, Integer, String
from config.db import meta

tipo_sanguineo = Table('tipos_sanguineos', meta,
                       Column('id', Integer, primary_key=True),
                       Column('nome', String))
