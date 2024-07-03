# Importando classes de seus respectivos módulos dentro do pacote atual. Fazemos, por padrão, o import relativo
from .gerenciador_entidades import GerenciadorEntidades

# Declarando quais classes serão importadas ao importar o pacote (através do comando from cursos_online.funcionalidades_auxiliares import *)
__all__ = ["GerenciadorEntidades"]
