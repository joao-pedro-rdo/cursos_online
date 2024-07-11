import streamlit as st

# from cursos_online.pages import *

st.set_page_config(
    page_title="Sistema de Cursos Online",
    page_icon=":mortar_board:",
    layout="wide",
    initial_sidebar_state="auto",
)


# Configuração da página
def pagina_inicial():

    # Título da página
    st.title("Bem-vindo ao Sistema de Cursos Online :mortar_board:")

    # Rodapé
    st.markdown("---")
    st.write("© 2024 Sistema de Cursos Online. Todos os direitos reservados.")


pagina_inicial()
