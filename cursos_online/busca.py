from cursos_online.funcionalidades_auxiliares import *

from cursos_online.usuarios import *
from cursos_online.cursos import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import streamlit as st

# Lista de classes
classes_a_serem_listadas = [Administrador, Aluno, Professor, Curso, Aula]
for classe in classes_a_serem_listadas:
    for instancia in classe.all():
        print(instancia.id)


# Exibir as classes usando st.write
st.write("Lista de Classes:")
for instancia in instancia:
    st.write(instancia)

#! Definicao da conecao com banco de dados e criacao das tabelas
 #! Definicao da conecao com banco de dados e criacao das tabelas
    GerenciadorEntidades.engine = create_engine(
        "mysql+pymysql://root:root@localhost/cursos_online"
    )
    GerenciadorEntidades.base.metadata.create_all(GerenciadorEntidades.engine)
    GerenciadorEntidades.session_maker = sessionmaker(bind=GerenciadorEntidades.engine)
    GerenciadorEntidades.session = GerenciadorEntidades.session_maker()