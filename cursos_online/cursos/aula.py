from cursos_online.funcionalidades_auxiliares.gerenciador_entidades import GerenciadorEntidades

# from cursos_online.cursos.curso import Curso

# importacao das bibliotecas da SQL
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

import datetime


class Aula(GerenciadorEntidades.base, GerenciadorEntidades):
    # Definiçao nome da tebela
    __tablename__ = "aulas"

    # Define as colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    criado_em = Column(DateTime, nullable=False)
    atualizado_em = Column(DateTime, nullable=False)
    url = Column(String(250), nullable=False)

    id_curso = Column(Integer, ForeignKey("cursos.id"), nullable=False)

    curso = relationship("Curso", back_populates="aulas")

    def __init__(self, curso, nome: str = "", url: str = ""):
        self.nome = nome
        self.url = url
        self.criado_em = datetime.datetime.now()
        self.atualizado_em = datetime.datetime.now()
        self.id_curso = curso.id

        GerenciadorEntidades.__init__(self)

    @property
    def curso(self):
        Curso = next(subclasse for subclasse in list(GerenciadorEntidades.__subclasses__()) if subclasse.__name__ == "Curso")
        return [curso for curso in Curso.all() if curso.id == self.id_curso][0]
