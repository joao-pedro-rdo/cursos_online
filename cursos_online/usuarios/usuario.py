# Minha Docstring
"""
oq tem no arquivo e praa que serve (Este modulo ...)
Classe pai que implementa a maior parte dos atributos e metodos de todos os usuarios do cursos_online 
"""
# Importação da classe que faz o CRUD nas demais classes
from cursos_online.funcionalidades_auxiliares.gerenciador_entidades import GerenciadorEntidades

# Importação das bibliotecas da SQL
from sqlalchemy import Column, Integer, String

from hashlib import sha256


class Usuario(GerenciadorEntidades.base, GerenciadorEntidades):

    # Definição nome da tabela
    __tablename__ = "usuarios"  # ? Essa nomeclatura "__tablename__" é padrao ou eu posso definir

    # Define as colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(String(200), nullable=False)
    cpf = Column(String(50), nullable=False)

    # Construtor, str =  " " type hint para usar dica do parametro mas pode usar outra coisa dica mesmo, e o = " " é o valor padrao
    def __init__(self, email: str = "", senha: str = "", nome: str = "", cpf: str = ""):
        """
        Inicialização dos objetos do usuario
        """
        # Atributos da classe
        self.email = email
        self.cpf = cpf
        self.nome = nome
        self.senha = senha

        # Certos atributos que precisam ser adicionados posteriormente à classe Usuario. Esses atributos não foram
        # adicionados ainda pois a implementação deles requer certos códigos que podem conflitar com a implementação existente.
        # Exemplos de atributos que precisam ser adicionados posteriormente: criado_em, atualizado_em

        # Calling the parent class initializer to register the object into the instances list of the class
        GerenciadorEntidades.__init__(self)

    #! Nao testado
    @classmethod
    def validacao_email(cls, email: str, usuario_existente: object = None) -> bool:
        email_is_valid = "@" in email and "." in email and not any(user.email == email for user in User.all() if user != usuario_existente)
        return email_is_valid

    @classmethod
    def validacao_senha(cls, senha: str) -> bool:
        senha_valida = len(senha) >= 5
        return senha_valida

    @classmethod
    def validacao_nome(cls, nome: str) -> bool:
        nome_valido = all(substring.isalpha() for substring in nome.split(" "))
        return nome_valido

    @classmethod
    def criacao_senha_hash(cls, senha: str) -> str:
        senha_bytes = senha.encode("utf-8")
        hash = sha256(senha_bytes)
        # Gera o hash em formato hexadecimal
        senha_hash = hash.hexdigest()
        return senha_hash

    @classmethod
    def autenticar(cls, email: str, senha: str) -> object:
        Aluno = next(subclasse for subclasse in list(Usuario.__subclasses__()) if subclasse.__name__ == "Aluno")
        Professor = next(subclasse for subclasse in list(Usuario.__subclasses__()) if subclasse.__name__ == "Professor")
        Administrador = next(subclasse for subclasse in list(Usuario.__subclasses__()) if subclasse.__name__ == "Administrador")

        print("SOU O ALUNO  ALL", Aluno.all())

        print("Senha enviada = ", senha)
        print("Senha hash enviada = ", Usuario.criacao_senha_hash(senha))
        for usuario in Usuario.all() + Aluno.all() + Professor.all() + Administrador.all():
            print("Senha usuario = ", usuario.senha)
            print("SAAAenha hash usuario = ", Usuario.criacao_senha_hash(usuario.senha))

        return next(
            (
                usuario
                for usuario in Usuario.all() + Aluno.all() + Professor.all() + Administrador.all()
                if usuario.email == email and Usuario.criacao_senha_hash(senha=senha) == usuario.senha
            ),
            None,
        )

    @classmethod
    def retorna_id_peloNome(cls, nome: str) -> int:
        return next(usuario.id for usuario in cls.all() if usuario.nome == nome)
