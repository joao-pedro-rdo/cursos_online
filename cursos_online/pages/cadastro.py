from cursos_online.funcionalidades_auxiliares import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from cursos_online.usuarios import *
from cursos_online.cursos import *

from faker import Faker
import streamlit as st

st.set_page_config(
    page_title="Criar Conta",
    page_icon=":mortar_board:",
    layout="centered",
    initial_sidebar_state="auto",
)


def criar_conta():
    faker = Faker(locale="pt_BR")

    st.title("Cadastro de Usuário")

    name = st.text_input("Nome")
    email = st.text_input("Email")
    cpf = st.text_input("CPF")
    senha = st.text_input("Senha", type="password")
    senha = Usuario.criacao_senha_hash(senha)
    if st.button("Cadastrar como Aluno"):
        if name and email and senha:
            new_user = Aluno(email=email, senha=senha, nome=name, cpf=cpf)
            st.success("Usuário cadastrado com sucesso!")
    if st.button("Cadastrar como Professor"):
        if name and email and senha:
            new_user = Professor(email=email, senha=senha, nome=name, cpf=cpf)
            st.success("Usuário cadastrado com sucesso!")
    if st.button("Cadastrar como Administrador"):
        if name and email and senha:
            new_user = Administrador(email=email, senha=senha, nome=name, cpf=cpf)
            st.success("Usuário cadastrado com sucesso!")

        else:
            st.error("Por favor, preencha os campos corretamente.")
            # st.success('Usuário cadastrado com sucesso!')
    else:
        st.error("Por favor, preencha todos os campos.")
    if st.button("Login"):
        st.switch_page("pages/login.py")


criar_conta()

#! Definicao da conecao com banco de dados e criacao das tabelas
GerenciadorEntidades.engine = create_engine("mysql+pymysql://root:root@localhost/cursos_online")
GerenciadorEntidades.base.metadata.create_all(GerenciadorEntidades.engine)
GerenciadorEntidades.session_maker = sessionmaker(bind=GerenciadorEntidades.engine)
GerenciadorEntidades.session = GerenciadorEntidades.session_maker()
