from sqlalchemy import Table, Column, Integer, ForeignKey
from app.sql_app.database import meta

competencias_perfil = Table('competencias_perfis', meta,
                 Column('competencia_id', Integer, ForeignKey('competencias.id')),
                 Column('perfil_id', Integer, ForeignKey('perfis.id')))
