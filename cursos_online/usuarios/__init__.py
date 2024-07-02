"""
    Este arquivo serve para importar as classes herdadas de usuario
"""

from .administrador import Administrador  # "."  Para fazer import relativo
from .aluno import Aluno
from .professor import Professor
from .user import User
from .entity_manager import EntityManager


__all__ = ['Administrador', 'Aluno', 'Professor', 'User', 'EntityManager']
