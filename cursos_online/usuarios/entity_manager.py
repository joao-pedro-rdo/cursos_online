from sqlalchemy.orm import declarative_base
from sqlalchemy import func


#! Classe pai de todos
class EntityManager:
    """Essa classe prove as principais funcionalidades bases para as demais classes"""

    base = declarative_base()  # ? NAO SEI PRA QUE SERVE ISSO

    def __init__(self) -> object:
        """Inicializa o objeto e registra na base de dados"""

    self.id = EntityManager.session.query(func.count(self.__class__.id)).scalar() + 1
    # 'self.__class__' é uma forma de referir-se à classe da instância atual
    # 'func.count(self.__class__.id)' é uma chamada para a função SQL COUNT, que conta o número de valores não-nulos na coluna id da tabela correspondente à classe.
    # 'session.query' cria uma consulta
    print(f"Instância {self} criada com sucesso.")
    # Adiciona a instancia ao bd
    EntityManager.session.add(self)

    # Confirma
    EntityManager.session.commit()

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
        return EntityManager.session.query(cls).all()

    @classmethod
    def update(cls, id: int, new_attributes: dict):
        """Updates an instance based on its ID and a dictionary with the new attributes.

        Args:
            id (int): ID of the instance to be updated.
            new_attributes (dict): Dictionary with the new attributes.
        """
        # Gathering the instance by its ID
        instance = EntityManager.session.query(cls).filter(cls.id == id).first()

        # If the instance exists, update its attributes
        if instance:
            for attribute_name, attribute_value in new_attributes.items():
                if hasattr(instance, attribute_name):
                    setattr(instance, attribute_name, attribute_value)

            # Confirming the transaction
            EntityManager.session.commit()
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
        instance = EntityManager.session.query(cls).filter(cls.id == id).first()

        if instance:
            # Removing the instance from the database
            EntityManager.session.delete(instance)

            # Confirming the transaction
            EntityManager.session.commit()

            print(f"Instância {id} deletada com sucesso.")
        else:
            print(f"Instância com ID {id} não encontrada.")
