import streamlit as st
import pyrebase
from firebase_config import firebase_config

# Inicializar Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

st.set_page_config(page_title="Entre na sua Conta", page_icon="👤", layout="centered")

# CSS
st.markdown("""
<style>
.box {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 20px;
    box-shadow: 2px 1px 10px gray;
}
.box > img {
    border-radius: 50%;
}
</style>
""", unsafe_allow_html=True)

# HTML
st.markdown("""
<div class="box">
    <img src="https://img.freepik.com/vector-premium/ilustracion-plana-vectorial-escala-grises-icono-perfil-usuario-avatar-persona-imagen-perfil-silueta-genero-neutral-apto-perfiles-redes-sociales-iconos-protectores-pantalla-como-plantillax9xa_719432-1061.jpg" width="150"/>
    <h1>Olá, visitante!</h1>
</div>
""", unsafe_allow_html=True)

# Botão para login com o Google
login_button = st.button("Entrar com Google", icon=":material/g_translate:", use_container_width=True, type="primary")

if login_button:
    try:
        # Redirecionamento para autenticação com Google
        user = auth.sign_in_with_email_and_password("email@example.com", "password")
        st.success(f"Bem-vindo(a), {user['email']}!")
    except Exception as e:
        st.error(f"Erro ao fazer login: {e}")
