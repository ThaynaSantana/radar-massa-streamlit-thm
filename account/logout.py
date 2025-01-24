import streamlit as st
import pyrebase
from firebase_config import firebase_config

# Inicializar Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Logout
st.set_page_config(page_title="Logout", page_icon="🚪", layout="centered")

st.title("🚪 Logout")

# Logout do Firebase
if st.button("Sair"):
    try:
        st.session_state["logged_in"] = False
        st.session_state["user"] = None
        st.success("Você saiu com sucesso!")
        st.experimental_set_query_params(page="main")  # Redireciona para a página principal
    except Exception as e:
        st.error(f"Erro ao sair: {e}")
