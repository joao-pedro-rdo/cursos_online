# Minha Docstring
"""
oq tem no arquivo e praa que serve (Este modulo ...)
Classe pai que implementa a maior parte dos atributos e metodos de todos os usuarios do cursos_online 
"""
# Importação da classe que faz o crud nas demais classes
from entity_manager import EntityManager

# Importação da bib time
from time import time

# ? Preciso instalar essas paradas no meu poetry ?
# Importação
from hashlib import sha256


class User(EntityManager):
    """
    Classe pai para ser usada com a herança
    """

    # ? Porque fazemmos isso afinal ???

    def __init__(  # Construtor, str =  " " type hint para usar dica do parametro mas pode usar outra coisa dica mesmo, e o = " " é o valor padrao
        self,
        email: str = "",
        cpf: str = "",
        nome: str = "",
        data_nascimento: str = "",
        senha: str = "",
    ):
        # ? porque tem outras função que usa "->"
        """
        Inicialização dos objetos do user
        """
        # TODO USAR HASH PARA ESCONDER A SENHA
        self.criado_em = time()
        self.atualizado_em = time()
        self.email = email
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.senha = senha

        # Calling the parent class initializer to register the object into the instances list of the class
        super().__init__() @ classmethod  # ? DE ONDE VEM ESSA CLASSE

        # TODO: AINDA FALTA IMPLMENTAR OS METODOS DO USER.PY
