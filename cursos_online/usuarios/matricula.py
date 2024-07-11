from cursos_online.funcionalidades_auxiliares.gerenciador_entidades import GerenciadorEntidades
from cursos_online.cursos.curso import Curso
from cursos_online.usuarios.aluno import Aluno

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


#! ============================================================ MUDAR ESSE ARQUIVO PARA O PACOTE CURSOS


class Matricula(GerenciadorEntidades.base, GerenciadorEntidades):

    # Definindo nome da tabela no banco de dados
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, autoincrement=True)

    id_curso = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    id_aluno = Column(Integer, ForeignKey("alunos.id"), nullable=False)

    curso = relationship("Curso", back_populates="matriculas")
    aluno = relationship("Aluno", back_populates="matriculas")

    def __init__(self, curso, aluno):
        self.id_curso = curso.id
        self.id_aluno = aluno.id
        GerenciadorEntidades.__init__(self)

    # Simula um atributo que retorna o curso associado à matrícula (É acessado como se fosse um atributo)
    @property
    def curso(self):
        return [curso for curso in Curso.all() if curso.id == self.id_curso][0]

    @property
    def aluno(self):
        return [aluno for aluno in Aluno.all() if aluno.id == self.id_aluno][0]
