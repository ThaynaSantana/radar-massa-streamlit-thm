import streamlit as st
import pandas as pd
import plotly.express as px
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
    # Plotly
    # Grafico1:
    fig1 = px.scatter(df, 
                      x='ano', 
                      y='gols', 
                      color='ano', 
                      title='Distribuição de Gols por Ano',
                      labels={"ano": "Ano", "gols": "Gols"})
    st.plotly_chart(fig1)
    
    # Gráfico2:
    fig2 = px.scatter(
        df,
        x='passes_totais',
        y='duelos_ganhos',
        color='ano',
        title='Passes precisos vs Duelos ganhos',
        hover_data=['ano', 'gols']
    )
    st.plotly_chart(fig2)
    
    # Grafico3:
    fig3 = px.scatter(
        df,
        x='ano',
        y='assistencias',
        color='time_alvo',
        title='Evolução de Assistencias ao Longo do Tempo',
        labels={"ano": "Ano", "assistencias": "Assistencias"}
    )
    st.plotly_chart(fig3)
else:
    st.info("Carregue uma base de dados para começar sua Analise de Desempenho")