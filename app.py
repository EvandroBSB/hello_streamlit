import streamlit as st

st.title("Minha primeira aplicação")

st.title("Agora vai...")

nome_usuario = st.text_input("Digite seu nome:" ,"")

if (nome_usuario != ''):
    st.text("Olá {}!!!".format(nome_usuario))