from cursos_online.funcionalidades_auxiliares import *

from cursos_online.usuarios import *
from cursos_online.cursos import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from faker import Faker
from random import choice

import streamlit.web.cli as stcli
from os import path


def main():
    faker_instance = Faker(locale="pt_BR")
    Administrador(
        email="123@gmail.com",
        senha=Usuario.criacao_senha_hash(senha="123"),
        nome=faker_instance.name(),
        cpf=faker_instance.cpf(),
    )


    arquivo_streamlit = path.join(path.dirname(__file__), "pagina_inicial.py")

    if not path.isfile(arquivo_streamlit):
        raise FileNotFoundError(f"O arquivo {arquivo_streamlit} não foi encontrado.")
    stcli.main_run([arquivo_streamlit])


if __name__ == "__main__":
    #! Definicao da conecao com banco de dados e criacao das tabelas
    GerenciadorEntidades.engine = create_engine("mysql+pymysql://root:root@localhost/cursos_online")
    GerenciadorEntidades.base.metadata.create_all(GerenciadorEntidades.engine)
    GerenciadorEntidades.session_maker = sessionmaker(bind=GerenciadorEntidades.engine)
    GerenciadorEntidades.session = GerenciadorEntidades.session_maker()

    # Running the main function
    main()
