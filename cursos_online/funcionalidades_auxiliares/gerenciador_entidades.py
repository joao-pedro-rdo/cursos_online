from sqlalchemy.orm import declarative_base
from sqlalchemy import func


class GerenciadorEntidades:
    """Essa classe prove as principais funcionalidades bases para as demais classes."""

    # Defininado variavel que controla se o usuario esta logado ou nao
    usuario_logado = None

    # Definindo a base de dados (padrão do SQLAlchemy)
    base = declarative_base()

    def __init__(self) -> object:
        """Inicializa o objeto e registra na base de dados"""
        # print("TESTE: ", GerenciadorEntidades.session.query(func.count(self.__class__.id)))
        self.id = GerenciadorEntidades.session.query(func.count(self.__class__.id)).scalar() + 1

        # 'self.__class__' é uma forma de referir-se à classe da instância atual
        # 'func.count(self.__class__.id)' é uma chamada para a função SQL COUNT, que conta o número de valores não-nulos na coluna id da tabela correspondente à classe.
        # 'session.query' cria uma consulta
        print(f"Instância {self} criada com sucesso.")
        # Adiciona a instancia ao bd

        GerenciadorEntidades.session.add(self)

        # Confirma
        GerenciadorEntidades.session.commit()

    def __str__(self) -> str:
        """Defines how the object is represented inside print statements.

        Returns:
            obj (str): Object representation
        """
        return f"{self.__class__.__name__}_{self.id}"

    def __repr__(self) -> str:
        """Defines how the object is represented inside the console.

        Returns:
            str: Object representation.
        """
        return f"{self.__class__.__name__}_{self.id}"

    @classmethod
    def all(cls) -> list:
        """Retorna a lista de todos os obejtos criados nas classe."""
        return GerenciadorEntidades.session.query(cls).all()

    @classmethod
    def update(cls, id: int, new_attributes: dict):
        """Updates an instance based on its ID and a dictionary with the new attributes.

        Args:
            id (int): ID of the instance to be updated.
            new_attributes (dict): Dictionary with the new attributes.
        """
        # Gathering the instance by its ID
        instance = GerenciadorEntidades.session.query(cls).filter(cls.id == id).first()

        # If the instance exists, update its attributes
        if instance:
            for attribute_name, attribute_value in new_attributes.items():
                if hasattr(instance, attribute_name):
                    setattr(instance, attribute_name, attribute_value)

            # Confirming the transaction
            GerenciadorEntidades.session.commit()
            print(f"Instância {instance} atualizada com sucesso.")
        else:
            print(f"Instância com ID {id} não encontrada.")

    @classmethod
    def delete(cls, id: int):
        """Remove as instancias do BD baseado no ID
        Args:
            id (int): ID da instancia para ser removida.
        """
        # Gathering the instance by its ID
        instance = GerenciadorEntidades.session.query(cls).filter(cls.id == id).first()

        if instance:
            # Removing the instance from the database
            GerenciadorEntidades.session.delete(instance)

            # Confirming the transaction
            GerenciadorEntidades.session.commit()

            print(f"Instância {id} deletada com sucesso.")
        else:
            print(f"Instância com ID {id} não encontrada.")

    @staticmethod
    def verifica_autenticacao():
        """Verifica se o usuario esta autenticado"""
        if GerenciadorEntidades.usuario_logado != None:
            return True
        return False

    @staticmethod
    def tipo_usuario_logado():
        """Retorna o tipo do usuario logado"""
        return type(GerenciadorEntidades.usuario_logado)

    @staticmethod
    def retorna_id(cls, id: int):
        return GerenciadorEntidades.session.query(cls).filter(cls.id == id).first()
