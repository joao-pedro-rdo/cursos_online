from cursos_online.funcionalidades_auxiliares import *

from cursos_online.usuarios import *
from cursos_online.cursos import *

from faker import Faker
import streamlit as st

def entrar():
    st.title("Login Page")

    email = st.text_input("Email")
    senha = st.text_input("Senha", type='password')

    if st.button("Login"): 
        if Usuario.autenticar(email=email, senha=senha):
            st.success("Logged In as {}".format(email))
        # Aqui você pode adicionar o código para o que deseja fazer após o login bem-sucedido
        else:
            print("Fodase")
            st.warning("fodase Incorrect email/Password")
def criar_conta():
    faker = Faker(locale="pt_BR")

    st.title("Cadastro de Usuário")

    name = st.text_input("Nome", value=faker.name())
    email = st.text_input("Email", value=faker.email())
    cpf = st.text_input("CPF", value=faker.cpf())
    senha = st.text_input("Senha", type="password", value=faker.password())

    if st.button("Cadastrar"):
        if name and email and senha:
            # Funçao a ser implementada de validacao de email, senha e nome
            # if Aluno.validacao_email(email) and Aluno.validacao_senha(password) and Aluno.validacao_nome(name):
            new_user = Aluno(email=email, senha=senha, nome=name, cpf=cpf)
            st.success("Usuário cadastrado com sucesso!")

        else:
            st.error("Por favor, preencha os campos corretamente.")
            # st.success('Usuário cadastrado com sucesso!')
    else:
        st.error("Por favor, preencha todos os campos.")
entrar()