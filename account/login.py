import streamlit as st
import pyrebase
from firebase_config import firebase_config

# Inicializar Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

st.set_page_config(page_title="Login com Google", page_icon="🔑", layout="centered")

# Página de login
st.title("🔑 Login com Google")

# Botão para login com o Google
login_button = st.button("Entrar com Google", icon=":material/g_translate:")

if login_button:
    try:
        # Redirecionamento para autenticação com Google
        user = auth.sign_in_with_email_and_password("email@example.com", "password")
        st.success(f"Bem-vindo(a), {user['email']}!")
    except Exception as e:
        st.error(f"Erro ao fazer login: {e}")
