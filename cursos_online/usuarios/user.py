# Minha Docstring
"""
oq tem no arquivo e praa que serve (Este modulo ...)
Classe pai que implementa a maior parte dos atributos e metodos de todos os usuarios do cursos_online 
"""
# Importação da classe que faz o crud nas demais classes
from .entity_manager import EntityManager

# Importação
#from hashlib import sha256

#importacao das bibliotecas da SQL
from sqlalchemy import Column, Integer, String, Date, DateTime
# from sqlalchemy.orm import declarative_base

# class User():
class User(EntityManager.base, EntityManager):
    """
    Classe pai para ser usada com a herança
    MELHORAR EXPLICAO DA ORM
    """

    # Definiçao nome da tebela 
    __tablename__ = 'usuarios'  #? Essa nomeclatura "__tablename__" é padrao ou eu posso definir 

    # Define as colunas da tabela 
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    # data_nascimento = Column(Date)
    senha = Column(String(50), nullable=False)  #? COMO QUE FAZ PARA HASHEAR
    cpf = Column(String(50), nullable=False)
    # criado_em = Column(DateTime, nullable=False)
    # atualizado_em = Column(DateTime, nullable=False)
    
    # Construtor, str =  " " type hint para usar dica do parametro mas pode usar outra coisa dica mesmo, e o = " " é o valor padrao
    def __init__(self, email: str = "", senha: str = "", nome: str = "",  data_nascimento: str = "", cpf:  str = ""):
        """
        Inicialização dos objetos do user
        """
        # Atributos da classe 
        # self.criado_em = time()
        # self.atualizado_em = time()
        self.email = email
        self.cpf = cpf
        self.nome = nome
        # self.data_nascimento = data_nascimento
        self.senha = senha

        # Calling the parent class initializer to register the object into the instances list of the class
        # super().__init__() #? super().__init__ OU ISSO AI 
        EntityManager.__init__(self)

    def porra(self):
        print("HELO WORD: Estou instaciado")
        return None

