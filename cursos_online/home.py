import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Sistema de Cursos Online",
    page_icon=":mortar_board:",
    layout="centered",
    initial_sidebar_state="auto",
)

# Título da página
st.title("Bem-vindo ao Sistema de Cursos Online :mortar_board:")

# Descrição
st.write(
    """
    Nosso sistema oferece uma variedade de cursos online para você aprimorar suas habilidades e conhecimentos. 
    Explore nossos cursos e comece a aprender hoje mesmo!
"""
)

# Botão para explorar cursos
if st.button("Explorar Cursos"):
    st.write("Aqui você pode encontrar uma lista de todos os nossos cursos disponíveis. [Funcionalidade em desenvolvimento]")

# Lista de cursos em destaque
st.header("Cursos em Destaque")
cursos_em_destaque = [
    {"nome": "Curso de Python para Iniciantes", "descricao": "Aprenda os fundamentos da programação em Python."},
    {"nome": "Desenvolvimento Web com Django", "descricao": "Crie aplicações web robustas usando o framework Django."},
    {"nome": "Machine Learning com Scikit-Learn", "descricao": "Descubra o mundo do Machine Learning com este curso prático."},
]

for curso in cursos_em_destaque:
    st.subheader(curso["nome"])
    st.write(curso["descricao"])

# Rodapé
st.markdown("---")
st.write("© 2024 Sistema de Cursos Online. Todos os direitos reservados.")
