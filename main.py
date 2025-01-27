import streamlit as st
import pyrebase
from firebase_config import firebase_config

# Configuração inicial
st.logo("src/logo.png", link="https://thmestatistica.com/")

# Inicializar Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

# Gerenciar estado de login no session_state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["user"] = None


# Pages Dashboard
jsonDashboard = [
            st.Page("pages/home.py", title="🏠 Home"),
            st.Page("pages/news.py", title="📰 Notícias do Dia"),
            st.Page("pages/analise.py", title="📊 Análise de Desempenho"),
            st.Page("pages/radar.py", title="📟 Radar Massa - A IA Verde"),
            #st.Page("conclusoes.py", title="📈 Tire suas próprias Conclusões!"),
            st.Page("pages/calendar.py", title="🗓️ Calendário de Jogos"),
]

# Navigation
if st.session_state['logged_in']:
    pages = {
        "Account": [
            st.Page("account/logout.py", title="Login", icon=":material/login:")
        ],
        "Dashboard": jsonDashboard,
    }
else:
    pages = {
        "Account": [
            st.Page("account/login.py", title="Login", icon=":material/login:")
        ],
        "Dashboard": jsonDashboard,
    }

pg = st.navigation(pages)
pg.run()
