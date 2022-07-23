from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime
from config.db import meta

experiencia = Table('experiencias', meta,
                    Column('id', Integer, primary_key=True),
                    Column('perfil_id', Integer, ForeignKey('perfis.id')),
                    Column('empresa', String),
                    Column('inicio', DateTime),
                    Column('fim', DateTime),
                    Column('atual_trabalho', Integer),
                    Column('cargo', String))
