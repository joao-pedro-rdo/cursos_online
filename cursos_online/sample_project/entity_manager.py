# Importing third-party libraries
from sqlalchemy.orm import declarative_base
from sqlalchemy import func


class EntityManager:
    """This class provides auxiliary methods that facilitate object manipulation."""

    base = declarative_base()

    def __init__(self) -> object:
        """Initializes the object and registers it in the database.

        Returns:
            object: Instance of the class being instantiated.
        """
        print("pqp")
        self.id = EntityManager.session.query(func.count(self.__class__.id)).scalar() + 1

        print(f"Instância {self} criada com sucesso.")
        # Adding the instance to the database
        EntityManager.session.add(self)

        # Confirming the transaction
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
        """Returns the list of created objects of a given class.

        Returns:
            list: List of objects from a given class.
        """
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
        """Removes an instance from the database based on an specific ID.

        Args:
            id (int): ID of the instance to be removed.
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
