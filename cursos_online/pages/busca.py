from cursos_online.funcionalidades_auxiliares import *

from cursos_online.usuarios import *
from cursos_online.cursos import *

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st


def ver_alunos():

    # Lista de classes
    tabela_alunos = []
    for i in Aluno.all():
        aux = [i.id, i.nome, i.email, i.cpf, i.senha]
        tabela_alunos.append(aux)

    st.dataframe(tabela_alunos)
    st.markdown("---")


def ver_professores():
    st.subheader("Proferores")
    tabela_professores = []
    for i in Professor.all():
        aux = [i.id, i.nome, i.email, i.cpf, i.senha]
        tabela_professores.append(aux)

    st.dataframe(tabela_professores)
    st.markdown("---")


def ver_administradores():
    st.subheader("Administradores")
    tabela_adminstradores = []
    for i in Administrador.all():
        aux = [i.id, i.nome, i.email, i.cpf, i.senha]
        tabela_adminstradores.append(aux)

    st.dataframe(tabela_adminstradores)


def ver_cursos():
    st.subheader("Cursos")
    tabela_cursos = []

    for i in Curso.all():
        aux = {
            "Nome": i.nome,
            "id": i.id,
            "Descricao": i.decricao,
            "Professor": i.id_professor,
            "Administrador": i.id_administrador,
            "Criado_em": i.criado_em,
            "Atualizado_em": i.atualizado_em,
        }
        tabela_cursos.append(aux)
    tabela_cursos = pd.DataFrame(tabela_cursos)
    st.dataframe(tabela_cursos)
    st.write("-------------------------------------------------")


def ver_aulas():
    st.subheader("Aulas")
    tabela_aulas = []

    for i in Aula.all():
        aux = {
            "nome": i.nome,
            "url": i.url,
            "criado_em": i.criado_em,
            "atualizado_em": i.atualizado_em,
            "id_curso": i.curso.id,
        }
        tabela_aulas.append(aux)
    tabela_aulas = pd.DataFrame(tabela_aulas)
    st.dataframe(tabela_aulas)
    st.write("-------------------------------------------------")


def ver_matricula():
    st.subheader("matricula")
    tabela_matricula = []

    for i in Matricula.all():
        aux = {
            "id matricula": i.id,
            "id aluno": i.id_aluno,
            "id curso": i.id_curso,
        }
        tabela_matricula.append(aux)
    tabela_matricula = pd.DataFrame(tabela_matricula)
    st.dataframe(tabela_matricula)
    st.write("-------------------------------------------------")


#! Definicao da conecao com banco de dados e criacao das tabelas
GerenciadorEntidades.engine = create_engine("mysql+pymysql://root:root@mysql.local/cursos_online")
GerenciadorEntidades.base.metadata.create_all(GerenciadorEntidades.engine)
GerenciadorEntidades.session_maker = sessionmaker(bind=GerenciadorEntidades.engine)
GerenciadorEntidades.session = GerenciadorEntidades.session_maker()

ver_alunos()
ver_administradores()
ver_professores()
ver_cursos()
ver_aulas()
ver_matricula()
