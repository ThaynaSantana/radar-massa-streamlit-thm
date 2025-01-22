import streamlit as st
from streamlit_oauth import OAuthManager
import os

# Configuração OAuth
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = "http://localhost:8501/"

st.title("Login com Conta Google")

# Inicializa o gerenciador de OAuth
oauth_manager = OAuthManager(
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    redirect_uri=GOOGLE_REDIRECT_URI,
scopes=["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"],
)

# Pagina inicial com Login
if "user" not in st.session_state:
    st.session_state["user"] = None

if st.session_state["user"]:
    st.success(f"Bem-vindo, {st.session_state['user']['name']}!")
    st.image(st.session_state["user"]["picture"], width=100)
    if st.button("Logout"):
        st.session_state["user"] = None
        st.experimental_rerun()
else:
    if st.button("Login com Google"):
        auth_url = oauth_manager.get_authorization_url()
        st.experimental_set_query_params(redirected="true")
        st.write(f"[Clique aqui para autenticar]({auth_url})")
    
    # Verificar se foi redirecionado pelo Google
    query_params = st.experimental_get_query_params()
    if "redirected" in query_params:
        code = query_params.get("code", [None])[0]
        if code:
            token = oauth_manager.get_access_token(code)
            user_info = oauth_manager.get_user_info(token)
            st.session_state["user"] = {
                "name": user_info["name"],
                "email": user_info["email"],
                "picture": user_info["picture"],
            }
            st.experimental_rerun()