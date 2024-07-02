# Importando módulos e pacotes do projeto
from entity_manager import EntityManager

# Importando bibliotecas de terceiros
from sqlalchemy import Column, Integer, String


class User(EntityManager.base, EntityManager):
    """This class represents a user in the system."""

    # Defining the table name
    __tablename__ = "users"

    # Defining the table columns
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

    def __init__(self, name: str, email: str) -> object:
        """User object initialization method.

        Args:
            name (str): User name.
            email (str): User email.

        Returns:
            object: Initialized object instance.
        """
        self.name = name
        self.email = email

        # Calling the parent class (EntityManager) initialization method
        EntityManager.__init__(self)
