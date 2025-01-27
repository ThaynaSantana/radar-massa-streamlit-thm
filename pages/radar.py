import os
import time
import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.responses.response_parser import ResponseParser

# Configuração Inicial da pagina
st.set_page_config(page_title="Radar Massa - A IA Verde", page_icon="📟")
st.logo("https://a.espncdn.com/i/teamlogos/soccer/500/2029.png", size="large")

class StreamlitResponse(ResponseParser):
    def __init__(self, context) -> None:
        super().__init__(context)

    def format_dataframe(self, result):
        st.dataframe(result["value"])
        return

    def format_plot(self, result):
        st.image(result["value"])
        return

    def format_other(self, result):
        st.write(result["value"])
        return


col1, col2 = st.columns([1,5])

with col1:
    st.image(width=100,image="https://a.espncdn.com/i/teamlogos/soccer/500/2029.png")

with col2:
    st.header('THM Estatistica e Paulo Massini', divider="green")

# Title
st.title("📟Radar Massa - A IA Verde")

# Uploud File
uplouded_file = st.sidebar.file_uploader("📂 Carregue aqui seus dados (Excel ou CSV)", type=['csv', 'xlsx'])

# Verifica se a chave 'show_toast' já existe no session_state
if "show_toast" not in st.session_state:
    st.session_state["show_toast"] = True

# Exibe o toast apenas se for a primeira inicialização
if st.session_state["show_toast"]:
    st.toast("🤖 Bem-vindo ao 📟Radar Massa!")
    st.session_state["show_toast"] = False  # Evita que o toast seja exibido novamente

if uplouded_file:
    # Carregando os dados
    progress_text = "Carregando dados... Por favor aguarde."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(0.01)
    time.sleep(1)
    my_bar.empty()
    # Lendo CSV
    if uplouded_file.type == "text/csv":
        df = pd.read_csv(uplouded_file)
    else:
        df = pd.read_excel(uplouded_file, engine='openpyxl')
    

    with st.expander("🔎 Dataframe Preview"):
        st.write(df.head(5))

    query = st.text_area("🗣️ Digite sua pergunta...")
    container = st.container()

    if query:
        st.toast("🤖Estou pensando e analisando..")
        llm = OpenAI(api_token=st.secrets["OPENAI_API_KEY"],)
        query_engine = SmartDataframe(
            df,
            config={
                "llm": llm,
                "response_parser": StreamlitResponse,
            },
        )

        answer = query_engine.chat(query)
        # Resposta Texto
        st.write(answer)
else:
    st.info("Anexe um arquivo CSV para começar a utilizar a Inteligencia Artificial!")