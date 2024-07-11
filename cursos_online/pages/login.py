from cursos_online.funcionalidades_auxiliares import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cursos_online.usuarios import *
from cursos_online.cursos import *

from faker import Faker
import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon=":mortar_board:",
    layout="wide",
    initial_sidebar_state="auto",
)


def entrar():
    st.title("Login Page")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type="password")

    if st.button("Login"):
        if Usuario.autenticar(email=email, senha=senha):
            st.success("Logado com {}".format(email))
            # Salva o usuário logado na sessão
            GerenciadorEntidades.usuario_logado = Usuario.autenticar(email=email, senha=senha)
            print("Usuario logado nome = ", GerenciadorEntidades.usuario_logado.nome)
        else:
            st.warning("email/senha incorretos")

    if st.button("Criar conta"):
        st.switch_page("pages/cadastro.py")


entrar()


#! Definicao da conecao com banco de dados e criacao das tabelas
GerenciadorEntidades.engine = create_engine("mysql+pymysql://root:root@localhost/cursos_online")
GerenciadorEntidades.base.metadata.create_all(GerenciadorEntidades.engine)
GerenciadorEntidades.session_maker = sessionmaker(bind=GerenciadorEntidades.engine)
GerenciadorEntidades.session = GerenciadorEntidades.session_maker()
