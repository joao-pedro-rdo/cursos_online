from .usuario import Usuario

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Professor(Usuario):
    """Classe Herdada de usuario que representa o adm/criador/moderador dos cursos"""

    # Definindo nome da tabela no banco de dados
    __tablename__ = "professores"

    # Definindo colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    cpf = Column(String(50), nullable=False)

    # O atributo senha, que gera uma coluna do tipo string no banco de dados, armazena a senha
    # criptografada do usuário. Esta funcionalidade de criptografia de senha ainda deve ser implementada.
    senha = Column(String(200), nullable=False)

    curso = relationship("Curso", back_populates="professor")
    # Variável padrão do SQLAlchemy que define a identidade polimórfica da classe (em linhas gerais, define o tipo de herança do SQLAlchemy)
    __mapper_args__ = {"polymorphic_identity": "professores", "concrete": True}

    def __init__(self, email: str = "", senha: str = "", nome: str = "", cpf: str = ""):
        Usuario.__init__(self, nome=nome, email=email, cpf=cpf, senha=senha)
