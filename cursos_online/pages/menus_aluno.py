from cursos_online.funcionalidades_auxiliares import *

from cursos_online.usuarios import *
from cursos_online.cursos import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

from faker import Faker
import streamlit as st
import time

st.set_page_config(
    page_title="Menu Aluno",
    page_icon=":mortar_board:",
    layout="wide",
    initial_sidebar_state="auto",
)


def verificar_login():
    # Função que verifica se usuario esta logado e certifica que ele é um administrador
    if GerenciadorEntidades.verifica_autenticacao() and isinstance(GerenciadorEntidades.usuario_logado, Aluno):
        st.write("Usuário autenticado.")
    else:
        st.error("Usuário não autenticado ou nao tem permissao para acessar essa pagina.")
        time.sleep(1)
        st.switch_page("pages/login.py")


def menu_aluno():

    st.title("Menu Aluno")
    if st.button("Ver Cursos disponíveis"):
        ver_cursos_disponiveis()
    if st.button("Ver Cursos Matriculados"):
        ver_meus_cursos()
    if st.button("Sair"):
        GerenciadorEntidades.usuario_logado = None
        st.switch_page("pagina_inicial.py")
    if st.button("Matricular Curso"):
        # verificar_login()
        st.switch_page("pages/matricula.py")
    if st.button("Ver Aulas"):
        # verificar_login()
        ver_aulas()


def ver_meus_cursos():
    meus_cursos = []
    st.write("Cursos matriculados:")
    for curso in Curso.all():
        for matricula in Matricula.all():
            if (matricula.aluno.id == GerenciadorEntidades.usuario_logado.id) and (matricula.curso.id == curso.id):
                aux = {
                    "Nome usuario": GerenciadorEntidades.usuario_logado.nome,
                    "id_usuario": GerenciadorEntidades.usuario_logado.id,
                    "curso_id:": curso.id,
                    "nome": curso.nome,
                    "descricao": curso.decricao,
                    "att": curso.atualizado_em,
                    "criado": curso.criado_em,
                }
                meus_cursos.append(aux)
    data_meus_cursos = pd.DataFrame(meus_cursos)
    st.dataframe(data_meus_cursos)


def ver_cursos_disponiveis():
    cursos_dispoveis = []
    st.write("Cursos disponíveis:")
    for curso in Curso.all():
        aux = {
            "curso_id:": curso.id,
            "nome": curso.nome,
            "descricao": curso.decricao,
            "att": curso.atualizado_em,
            "criado": curso.criado_em,
        }
        cursos_dispoveis.append(aux)
    table = pd.DataFrame(cursos_dispoveis)
    st.dataframe(table)


def ver_aulas():
    aulas_do_aluno = []
    for curso in Curso.all():
        for matricula in Matricula.all():
            if (matricula.aluno.id == GerenciadorEntidades.usuario_logado.id) and (matricula.curso.id == curso.id):
                st.subheader(f"Curso: {curso.nome}")
                st.write(f"Descrição: {curso.decricao}")
                st.write(f"Professor: {curso.professor.nome}")
                st.write("Aulas:")
                for aula in curso.aulas:
                    aux = {
                        "Aula": aula.nome,
                        "URL": aula.url,
                    }
                    aulas_do_aluno.append(aux)
                table_aulas = pd.DataFrame(aulas_do_aluno)
                st.dataframe(table_aulas)
                st.write("-------------------------------------------------")


verificar_login()
menu_aluno()

#! Definicao da conecao com banco de dados e criacao das tabelas
GerenciadorEntidades.engine = create_engine("mysql+pymysql://root:root@172.25.0.3/cursos_online")
GerenciadorEntidades.base.metadata.create_all(GerenciadorEntidades.engine)
GerenciadorEntidades.session_maker = sessionmaker(bind=GerenciadorEntidades.engine)
GerenciadorEntidades.session = GerenciadorEntidades.session_maker()
