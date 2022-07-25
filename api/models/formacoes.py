from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sql_app.database import meta

formacoes = Table('formacao', meta,
                  Column('id', Integer, primary_key=True),
                  Column('instituicao_id', Integer, ForeignKey('instituicoes.id')),
                  Column('perfil_id', Integer, ForeignKey('perfis.id')),
                  Column('nome', String(255)))
