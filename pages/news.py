import re
import os
import time
import requests
from PIL import Image
import streamlit as st
from datetime import datetime

# Configuração inicial
st.set_page_config(page_title="Notícias do Dia", page_icon="📰", layout="centered")

# Request API de noticia
@st.cache_data
def request_api():
    API_KEY = st.secrets["NEWS_API_KEY"]
    url = f"https://newsapi.org/v2/everything?q=palmeiras&apiKey={API_KEY}&language=pt&sortBy=publishedAt"
    response = requests.get(url)
    return response 

# Se Status Code for 200, então a requisição foi bem sucedida
resposta = request_api()
if resposta.status_code == 200:
    # Conteúdo da resposta
    noticias = resposta.json()

# Função para exibir uma notícia
def exibir_noticia(titulo, descricao, conteudo, imagem_url=None, link=None, autor=None, data=None):
    st.subheader(titulo)
    st.write(descricao)
    if imagem_url:
        st.image(imagem_url, use_container_width=True)
    else:
        st.image("https://www.k-foodtrade.or.kr/com/imageView.do?catalogId=65218")
    st.write(f"Autor: {autor}")
    st.write(f"Data de publicação: {data}")
    st.write(conteudo)
    if link:
        st.markdown(f"[Saiba mais...]({link})")

# Título principal
st.title("📰 Notícias do Dia")
st.subheader("Aqui estão as notícias mais recentes do dia!", divider="blue")

# Exibir notícias
for noticia in noticias['articles']:
    with st.container():
        # formatação do content
        noticia["content"] = re.sub(r'\[\+\d+ chars\]', '', noticia["content"])
        if noticia["title"] == None:
            noticia["title"] = noticia['description'][:44] + "..."

        # Formatação da Data de publicacao
        data_publicacao = datetime.strptime(noticia["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
        noticia["publishedAt"] = data_publicacao.strftime("%d/%m/%Y - %H:%M")

        exibir_noticia(
            titulo=noticia['title'],
            descricao=noticia["description"],
            conteudo=noticia["content"],
            imagem_url=noticia["urlToImage"],
            link=noticia["url"],
            autor=noticia["author"],
            data=noticia["publishedAt"]
        )
        st.divider()
