from BancoFilmes.ORMs.Bases import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Boolean

class GenerosFilme(Base):
    __tablename__ = "generos_filme"

    id_genero = Column(Integer,primary_key=True)
    nome = Column(String)
    descricao = Column(String)


class Filmes(Base):
    __tablename__ = "filmes"

    id_filme = Column (Integer, primary_key=True)
    nome = Column(String)
    publicado_em = Column(DateTime)
    sinopse = Column(Text)
    idade_minima = Column(Integer)
    genero = Column(Integer, ForeignKey("generos_filme.id_genero"))
    em_3d = Column(Boolean)


def cria_tabelas(conexao):
    Base.metadata.create_all(conexao)
    