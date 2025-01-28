import pandas as pd
import streamlit as st

# Dados do calendário de jogos
data = {
    "data": ["02/02",
            "06/02",
            "09/02",
            "13/02",
            "16/02",
            "20/02",
            "23/02"],
    "horario": ["18:30",
                 "20:00",
                   "18:30",
                     "19:30",
                       "18:30",
                         "19:30",
                           "18:30"],
    "adversario": ['Guarani',
                    'Corinthians',
                      'Agua Santa',
                        'Internacional de Limeira',
                          'São paulo',
                            'Botafogo-SP',
                              'Mirassol'],
    "local": ['Brinco de Ouro',
               'Allianz Parque',
                 'Distrital do Inamar',
                   'Major Sobrinho',
                     'Allianz Parque',
                       'Allianz Parque',
                         'Estádio Campos Maia'],
    "onde_assistir": ["SporTV",
                       "Premiere",
                         "Globo",
                           "Premiere",
                               "Star+",
                                 "ESPN",
                                   "CaseTV"],
    "mes": ["Fevereiro 2025",
             "Fevereiro 2025",
               "Fevereiro 2025",
                 "Fevereiro 2025",
                   "Fevereiro 2025",
                     "Fevereiro 2025",
                       "Fevereiro 2025"],
    "logo": [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f7/Guarani_FC_%28E%29_-_SP.svg/180px-Guarani_FC_%28E%29_-_SP.svg.png",
        "https://upload.wikimedia.org/wikipedia/pt/thumb/b/b4/Corinthians_simbolo.png/180px-Corinthians_simbolo.png",
        "https://upload.wikimedia.org/wikipedia/pt/thumb/b/b8/Ecaguasanta.png/180px-Ecaguasanta.png",
        "https://upload.wikimedia.org/wikipedia/pt/thumb/5/5c/AAInternacional.png/180px-AAInternacional.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Brasao_do_Sao_Paulo_Futebol_Clube.svg/180px-Brasao_do_Sao_Paulo_Futebol_Clube.svg.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Botafogo_Futebol_Clube_%28Ribeir%C3%A3o_Preto%29_logo_%282021%29.png/180px-Botafogo_Futebol_Clube_%28Ribeir%C3%A3o_Preto%29_logo_%282021%29.png",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Mirassol_FC_logo.png/225px-Mirassol_FC_logo.png"
    ],
}
df = pd.DataFrame(data)

# Título da página
st.title("📅 Calendário de Jogos do Palmeiras")

# Menu de seleção do mês
meses = df["mes"].unique()
mes_selecionado = st.selectbox("Selecione o período:", meses)

# Filtrar jogos pelo mês selecionado
df_filtrado = df[df["mes"] == mes_selecionado]

# Exibição dos jogos filtrados
st.subheader(f"Jogos do Palmeiras em {mes_selecionado}")

if df_filtrado.empty:
    st.write("Nenhum jogo encontrado para este período.")
else:
    for _, row in df_filtrado.iterrows():
        with st.container():
            st.write("### 🗓️", row["data"])
            col1, col2, col3 = st.columns([1, 3, 1])

            # Logo do adversário
            with col1:
                st.image(row["logo"], width=60)

            # Informações do jogo
            with col2:
                st.write(f"**Adversário:** {row['adversario']}")
                st.write(f"**Local:** {row['local']}")
                st.write(f"**Horário:** {row['horario']}")

            # Botão para onde assistir
            with col3:
                if st.button(f"📺 Onde assistir ({row['adversario']})", key=row["data"]):
                    st.info(f"O jogo será transmitido em: {row['onde_assistir']}")

# Rodapé
st.markdown("---")
st.markdown("⚽ _Acompanhe todos os jogos do Verdão com a gente!_")
