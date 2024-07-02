from .user  import User

class Administrador(User):
    """ Classe Herdada de usuario que representa o adm/criador/moderador dos cursos"""
    # __tablename__ = 'adminstrador'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    # nome = Column(String(50), nullable=False)
    # email = Column(String(50), nullable=False)
    # senha = Column(String(50), nullable=False)  #? COMO QUE FAZ PARA HASHEAR
    # cpf = Column(String(50), nullable=False)
    

    def __init__(self, email: str = "", senha: str = "", nome: str = "", data_nascimento: str = "", cpf: str = ""):
        User.__init__(self, email, senha, nome, data_nascimento, cpf)
