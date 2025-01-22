import os
import time
import streamlit as st
import pandas as pd
import pandas.core.arrays
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.responses.response_parser import ResponseParser

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

st.header('THM Estatistica e Paulo Massini', divider="green")

main = st.container()
# Title
main.title("📟Radar Massa - A IA Verde")
# Uploud File
uplouded_file = st.sidebar.file_uploader("📂 Carregue aqui seus dados", type="csv")

# Dashboard
st.sidebar.title("Dashboard")
st.sidebar.button("🔍 Notícias Recentes", use_container_width=True)
st.sidebar.button("📊 Análise de Desempenho", use_container_width=True)
st.sidebar.button("📟 Radar Massa - A IA Verde", use_container_width=True)
st.sidebar.button("📈 Tire suas próprias Conclusões!", use_container_width=True)
st.sidebar.button("🗓️ Calendário de Jogos", use_container_width=True)

st.toast("🤖 Bem-vindo ao 📟Radar Massa!")

if uplouded_file:
    # Carregando os dados
    progress_text = "Carregando dados... Por favor aguarde."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(0.01)
    time.sleep(1)
    my_bar.empty()
    df = pd.read_csv(uplouded_file)

    with st.expander("🔎 Dataframe Preview"):
        st.write(df.head(5))

    query = st.text_area("🗣️ Digite sua pergunta...")
    container = st.container()

    if query:
        st.toast("🤖Estou pensando e analisando..")
        llm = OpenAI(api_token=os.environ["OPENAI_API_KEY"],)
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
    st.info("Anexe um arquivo CSV para começar")