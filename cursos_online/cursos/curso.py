from cursos_online.funcionalidades_auxiliares.gerenciador_entidades import GerenciadorEntidades

# importacao das bibliotecas da SQL
from sqlalchemy import (
    Column,
    Integer,
    String,
)  #! se  for adciionar outros tipos de dados tem que adcionar aqui

# from sqlalchemy.orm import declarative_base


# ? COMO QUE FAZ RELAÇAO ENTRE TABELAS ???????????????????
class Curso(GerenciadorEntidades.base, GerenciadorEntidades):
    # Definiçao nome da tebela
    __tablename__ = "cursos"  # ? Essa nomeclatura "__tablename__" é padrao ou eu posso definir

    # Define as colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    # criado_em = Column(DateTime, nullable=False)
    # atualizado_em = Column(DateTime, nullable=False)
    decricao = Column(String(250), nullable=False)

    # TODO: DEFINIR AS RELACOES COM OUTRAS TABELAS
    # ? TEM COMO MUDAR AS CORES PADRAO DESSES COMENTARIOS

    def __init__(self, nome: str = "", descricao: str = ""):
        self.nome = nome
        self.decricao = descricao

        GerenciadorEntidades.__init__(self)
