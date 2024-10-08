from cursos_online.funcionalidades_auxiliares.gerenciador_entidades import GerenciadorEntidades
from cursos_online.cursos.aula import Aula

# importacao das bibliotecas da SQL
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime


class Curso(GerenciadorEntidades.base, GerenciadorEntidades):
    # Definiçao nome da tebela
    __tablename__ = "cursos"  # ? Essa nomeclatura "__tablename__" é padrao ou eu posso definir

    # Define as colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    criado_em = Column(DateTime, nullable=False)
    atualizado_em = Column(DateTime, nullable=False)
    decricao = Column(String(250), nullable=False)

    id_professor = Column(Integer, ForeignKey("professores.id"), nullable=False)
    #!DESFAZER ADMINISTRADOR
    id_administrador = Column(Integer, ForeignKey("administradores.id"), nullable=False)

    professor = relationship("Professor", back_populates="curso")
    administrador = relationship("Administrador", back_populates="curso")
    aulas = relationship("Aula", back_populates="curso")

    def __init__(self, nome: str = "", descricao: str = "", id_professor: int = 0, id_administrador: int = 0):
        self.nome = nome
        self.decricao = descricao
        self.criado_em = datetime.datetime.now()
        self.atualizado_em = datetime.datetime.now()
        self.id_professor = id_professor
        self.id_administrador = id_administrador

        GerenciadorEntidades.__init__(self)

    # Lita de aulas do curso
    @property
    def aulas(self):
        return [aula for aula in Aula.all() if aula.curso == self]

    @property
    def alunos(self):
        Matricula = next(subclasse for subclasse in list(GerenciadorEntidades.__subclasses__()) if subclasse.__name__ == "Matricula")
        return [matricula.aluno for matricula in Matricula.all() if matricula.curso == self]

    @staticmethod
    def retorna_cls_peloNome(nome: str):
        return next(curso for curso in Curso.all() if curso.nome == nome)
