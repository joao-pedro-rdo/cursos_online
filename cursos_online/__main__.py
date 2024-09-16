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

    arquivo_streamlit = path.join(path.dirname(__file__), "pagina_inicial.py")

    if not path.isfile(arquivo_streamlit):
        raise FileNotFoundError(f"O arquivo {arquivo_streamlit} não foi encontrado.")
    stcli.main_run([arquivo_streamlit])


if __name__ == "__main__":
    #! Definicao da conecao com banco de dados e criacao das tabelas
    GerenciadorEntidades.engine = create_engine("mysql+pymysql://root:root@172.25.0.3/cursos_online")
    GerenciadorEntidades.base.metadata.create_all(GerenciadorEntidades.engine)
    GerenciadorEntidades.session_maker = sessionmaker(bind=GerenciadorEntidades.engine)
    GerenciadorEntidades.session = GerenciadorEntidades.session_maker()

    # Running the main function
    main()
