"""
    Este arquivo serve para importar as classes herdadas de usuario
"""

# Importando classes de seus respectivos módulos dentro do pacote atual. Fazemos, por padrão, o import relativo
# (com ponto inicial) para que o Python saiba que estamos importando de um módulo dentro do mesmo pacote.
from .administrador import Administrador
from .aluno import Aluno
from .professor import Professor
from .usuario import Usuario


__all__ = ["Usuario", "Administrador", "Aluno", "Professor"]
