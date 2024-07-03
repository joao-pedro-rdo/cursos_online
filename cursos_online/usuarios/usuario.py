# Minha Docstring
"""
oq tem no arquivo e praa que serve (Este modulo ...)
Classe pai que implementa a maior parte dos atributos e metodos de todos os usuarios do cursos_online 
"""
# Importação da classe que faz o CRUD nas demais classes
from cursos_online.funcionalidades_auxiliares.gerenciador_entidades import GerenciadorEntidades

# Importação das bibliotecas da SQL
from sqlalchemy import Column, Integer, String


class Usuario(GerenciadorEntidades.base, GerenciadorEntidades):
    """
    Classe pai para ser usada com a herança
    MELHORAR EXPLICAO DA ORM
    """

    # Definição nome da tabela
    __tablename__ = "usuarios"  # ? Essa nomeclatura "__tablename__" é padrao ou eu posso definir

    # Define as colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    senha = Column(String(50), nullable=False)
    cpf = Column(String(50), nullable=False)

    # Construtor, str =  " " type hint para usar dica do parametro mas pode usar outra coisa dica mesmo, e o = " " é o valor padrao
    def __init__(self, email: str = "", senha: str = "", nome: str = "", cpf: str = ""):
        """
        Inicialização dos objetos do user
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

    def porra(self):
        print("HELO WORLD: Estou instanciado")
        return None
