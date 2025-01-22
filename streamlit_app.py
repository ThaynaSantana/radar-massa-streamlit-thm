import os
import time
import streamlit as st
import pandas as pd
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


# Title
st.title("🤖BotPalmeiras Dataset🟢⚽")
# Uploud File
uplouded_file = st.sidebar.file_uploader("📂 Upload de Arquivo CSV", type="csv")
# Navigation pages
pg = st.navigation({
    "Sua Conta": [log_out, settings],
})
pg.run()

# Dashboard
st.sidebar.title("Dashboard")
st.sidebar.button("📊 Análise de Dados")
st.sidebar.button("📈 Visualização de Dados")
st.sidebar.button("🔍 Pesquisa de Dados")

st.toast("🤖 Bem-vindo ao BotPalmeiras Dataset!")

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

        answer = query_engine.chat(query, )
        st.write(answer)
else:
    st.info("Anexe um arquivo CSV para começar")