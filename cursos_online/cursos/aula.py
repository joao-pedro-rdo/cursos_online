from cursos_online.funcionalidades_auxiliares.gerenciador_entidades import (
    GerenciadorEntidades,
)

# importacao das bibliotecas da SQL
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime, 
    ForeignKey  
) 
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


    def __init__(self, nome: str = "", url: str = "", id_curso: int = 0):
        self.nome = nome
        self.url = url
        self.criado_em = datetime.datetime.now()
        self.atualizado_em = datetime.datetime.now()
        self.id_curso = id_curso

        GerenciadorEntidades.__init__(self)
    def separa_aula_curso(self, id_curso):
        """Essa função retorna uma lista de aulas de um curso específico"""
        return [aula for aula in Aula.all() if aula.id_curso == id_curso]