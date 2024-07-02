from .user  import User
class Aluno(User):
    def __init__(self, email: str = "", senha: str = "", nome: str = "", data_nascimento: str = "", cpf: str = ""):
        User.__init__(self, email, senha, nome, data_nascimento, cpf)