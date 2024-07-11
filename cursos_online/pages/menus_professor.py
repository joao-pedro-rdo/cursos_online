from cursos_online.funcionalidades_auxiliares import *

from cursos_online.usuarios import *
from cursos_online.cursos import *

import pandas as pd
import streamlit as st
import time


st.set_page_config(
    page_title="Menu Professor",
    page_icon=":mortar_board:",
    layout="wide",
    initial_sidebar_state="auto",
)


def verificar_login():
    # Função que verifica se usuario esta logado e certifica que ele é um administrador
    if GerenciadorEntidades.verifica_autenticacao() and isinstance(GerenciadorEntidades.usuario_logado, Professor):
        st.write("Usuário autenticado.")
    else:
        st.error("Usuário não autenticado ou nao tem permissao para acessar essa pagina.")
        time.sleep(1)
        st.switch_page("pages/login.py")


def adicionar_aula():
    nome_aula = st.text_input("Nome da aula:")
    url_aula = st.text_input("URL da aula:")

    lista_cursos = []
    for curso in Curso.all():
        if curso.id_professor == GerenciadorEntidades.usuario_logado.id:
            lista_cursos.append(curso)
    if len(lista_cursos) == 0:
        st.warning("Você não tem cursos associados.")
    nome_curso = st.selectbox("Cursos:", [curso.nome for curso in lista_cursos])

    obj_curso = Curso.retorna_cls_peloNome(nome_curso)

    if st.button("Cadastrar"):
        Aula(obj_curso, nome=nome_aula, url=url_aula)
        st.success("Curso cadastrado com sucesso.")


def ver_aulas_por_curso():
    for curso in Curso.all():
        aulas_cadastradas = []
        # percorre todos os cursos e verifica se o curso foi criado pelo administrador logado
        if curso.id_professor == GerenciadorEntidades.usuario_logado.id:
            st.subheader(f"Curso: {curso.nome}")
            st.write(f"Descrição: {curso.decricao}")
            st.write(f"Administrador: {curso.administrador.nome}")
            st.write("Aulas:")
            for aula in curso.aulas:
                aux = {
                    "Aula": aula.nome,
                    "URL": aula.url,
                }
                aulas_cadastradas.append(aux)
            table_aulas = pd.DataFrame(aulas_cadastradas)
            st.dataframe(table_aulas)
            st.write("-------------------------------------------------")
        table_aulas = pd.DataFrame()


verificar_login()
adicionar_aula()
ver_aulas_por_curso()
