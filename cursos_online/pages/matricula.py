from cursos_online.funcionalidades_auxiliares import *

from cursos_online.usuarios import *
from cursos_online.cursos import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

from faker import Faker
import streamlit as st
import time


def verificar_login():
    # Função que verifica se usuario esta logado e certifica que ele é um administrador
    if GerenciadorEntidades.verifica_autenticacao() == True and isinstance(GerenciadorEntidades.usuario_logado, Aluno):
        st.write("Usuário autenticado.")
    else:
        st.error("Usuário não autenticado ou nao tem permissao para acessar essa pagina.")
        time.sleep(1)
        st.switch_page("pages/login.py")


def matricular_curso():
    st.title("Matricular em Curso")
    st.write("Selecione o curso que deja se matricular:")

    nome_curso = st.selectbox("Curso:", [curso.nome for curso in Curso.all()])
    print("Nome do curso selecionado: ", nome_curso)
    print("Nome gerenciador ", GerenciadorEntidades.usuario_logado.nome)
    if st.button("Matricular"):
        for curso in Curso.all():
            if nome_curso == curso.nome:
                print("Matriculando...", GerenciadorEntidades.usuario_logado.nome, "no curso: ", curso.nome)
                Matricula(curso=curso, aluno=GerenciadorEntidades.usuario_logado)
                st.success("Curso cadastrado com sucesso.")
                break


verificar_login()
matricular_curso()


#! Definicao da conecao com banco de dados e criacao das tabelas
GerenciadorEntidades.engine = create_engine("mysql+pymysql://root:root@172.17.0.3/cursos_online")
GerenciadorEntidades.base.metadata.create_all(GerenciadorEntidades.engine)
GerenciadorEntidades.session_maker = sessionmaker(bind=GerenciadorEntidades.engine)
GerenciadorEntidades.session = GerenciadorEntidades.session_maker()
