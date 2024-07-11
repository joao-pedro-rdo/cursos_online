from cursos_online.funcionalidades_auxiliares import *

from cursos_online.usuarios import *
from cursos_online.cursos import *

import pandas as pd

import streamlit as st
import time


def verificar_login():
    # Função que verifica se usuario esta logado e certifica que ele é um administrador
    if GerenciadorEntidades.verifica_autenticacao() and isinstance(GerenciadorEntidades.usuario_logado, Administrador):
        st.write("Usuário autenticado.")
    else:
        st.error("Usuário não autenticado ou nao tem permissao para acessar essa pagina.")
        time.sleep(1)
        st.switch_page("pages/login.py")


def cadastrar_curso():
    st.title("Criar novo Curso")
    st.write("Preencha os campos abaixo para cadastrar um novo curso:")

    nome = st.text_input("Nome do Curso:")
    descricao = st.text_area("Descrição do Curso:")
    nome_professor = st.selectbox("Professor:", [professor.nome for professor in Professor.all()])

    id_professor = Professor.retorna_id_peloNome(nome_professor)

    if st.button("Cadastrar"):
        Curso(nome=nome, descricao=descricao, id_professor=id_professor, id_administrador=GerenciadorEntidades.usuario_logado.id)
        st.success("Curso cadastrado com sucesso.")


def ver_cursos_criados():
    st.title("Cursos Criados")

    for curso in Curso.all():
        alunos_matriculados = []
        aulas_cadastradas = []
        # percorre todos os cursos e verifica se o curso foi criado pelo administrador logado
        if curso.id_administrador == GerenciadorEntidades.usuario_logado.id:
            st.subheader(f"Curso: {curso.nome}")
            st.write(f"Descrição: {curso.decricao}")
            st.write(f"Professor: {curso.professor.nome}")

            st.write("Aulas:")

            for aula in curso.aulas:
                aux = {
                    "Aula": aula.nome,
                    "URL": aula.url,
                }
                aulas_cadastradas.append(aux)
            table_aulas = pd.DataFrame(aulas_cadastradas)
            st.dataframe(table_aulas)

            # Mostra a lista de alunos matriculados no curso
            st.write("Alunos Matriculados:")
            for aluno in curso.alunos:
                aux = {
                    "Aluno": aluno.nome,
                }
                alunos_matriculados.append(aux)
            table = pd.DataFrame(alunos_matriculados)
            st.dataframe(table)
            st.write("-------------------------------------------------")
        table_aulas = pd.DataFrame()
        table = pd.DataFrame()


verificar_login()
cadastrar_curso()
ver_cursos_criados()
