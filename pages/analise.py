import streamlit as st
import pandas as pd
import time

st.title("📊 Análise de Desempenho")

uplouded_file = st.sidebar.file_uploader("📂 Carregue aqui seus dados (Excel ou CSV)", type=['csv', 'xlsx', 'xls'])

if uplouded_file:
    # Carregando os dados
    progress_text = "Carregando dados... Por favor aguarde."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(0.01)
    time.sleep(1)
    my_bar.empty()
    
    # Lendo arquivo
    if uplouded_file.type == "text/csv":
        df = pd.read_csv(uplouded_file)
    else:
        df = pd.read_excel(uplouded_file, engine='openpyxl')
    
    with st.expander("Dataframe Preview", icon=":material/preview:"):
        st.dataframe(df)
    
    # Graficos
    st.bar_chart(df, x="nome_do_jogador", y="placar_casa", color='#00FFb0')
    st.line_chart(df, x="passes_totais", y="ano")
else:
    st.info("Carregue uma base de dados para começar sua Analise de Desempenho")