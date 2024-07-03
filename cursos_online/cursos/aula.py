from cursos_online.funcionalidades_auxiliares.gerenciador_entidades import (
    GerenciadorEntidades,
)

# importacao das bibliotecas da SQL
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,   
) 

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
    
    def __init__(self, nome: str = "", url: str = ""):
        self.nome = nome
        self.url = url
        self.criado_em = datetime.datetime.now()
        self.atualizado_em = datetime.datetime.now()

        GerenciadorEntidades.__init__(self)