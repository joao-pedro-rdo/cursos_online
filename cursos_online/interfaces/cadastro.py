"""
 Primeiros testes com a biblioteca Streamlit
"""
#! FALAR COM professpor

import streamlit as st
st.title('Cadastro de Usuário')

name = st.text_input('Nome')
email = st.text_input('Email')
password = st.text_input('Senha', type='password')

if st.button('Cadastrar'):
    if name and email and password:
        st.success('Usuário cadastrado com sucesso!')
    else:
        st.error('Por favor, preencha todos os campos.')