import streamlit as st

st.set_page_config(page_title="Spotify Analytics", layout="wide")

# =========================
# 🎨 ESTILO SPOTIFY
# =========================
st.markdown("""
<style>
body {
    background-color: #121212;
    color: white;
}
h1, h2, h3 {
    color: #1DB954;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🎧 HEADER COM LOGO
# =========================
col1, col2 = st.columns([1, 5])

with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg", width=80)

with col2:
    st.title("Spotify Analytics")
    st.markdown("### A Ciência por trás dos Hits")

st.divider()

# =========================
# 🎯 PROBLEMA
# =========================
st.header("🎯 Problema de Pesquisa")

st.markdown("""
Quais fatores fazem uma música se tornar um **Hit** na era do streaming?

Com milhões de músicas lançadas todos os anos, entender o que define o sucesso se tornou um desafio tanto acadêmico quanto de mercado.
""")

# =========================
# 🧠 METODOLOGIA
# =========================
st.header("🧠 Metodologia")

st.markdown("""
Este projeto utiliza conceitos de **Big Data e Machine Learning** para analisar padrões de sucesso musical.

A partir de dados inspirados na indústria (como Spotify), construímos um modelo capaz de estimar o sucesso de uma música com base em:

- Popularidade e número de streams  
- Crescimento e viralização  
- Engajamento (replay e compartilhamentos)  
- Rejeição (skip)  
- Presença em playlists  

Esses fatores são combinados em um indicador único: o **Score de Sucesso**.
""")

# =========================
# 📐 CÁLCULO
# =========================
st.header("📐 Como medimos o sucesso")

st.markdown("""
Criamos um **Score de Sucesso**, que representa o desempenho de uma música com base em múltiplas métricas.

Cada variável recebe um peso de acordo com sua relevância no mercado musical.
""")

st.latex(r'''
Score = 0.25 \cdot Streams + 0.20 \cdot Crescimento + 0.15 \cdot Replay + 0.15 \cdot (1 - Skip) + 0.15 \cdot Playlists + 0.10 \cdot Compartilhamentos
''')

st.markdown("""
### 🔍 Interpretação do modelo

- **Streams** → alcance da música  
- **Crescimento** → velocidade de viralização  
- **Replay** → retenção do público  
- **Skip** → rejeição (quanto menor, melhor)  
- **Playlists** → exposição  
- **Compartilhamentos** → engajamento social  

Antes do cálculo, todas as variáveis são **normalizadas**, garantindo equilíbrio entre elas.
""")

# =========================
# 🏆 HIT
# =========================
st.header("🏆 Definição de Hit")

st.markdown("""
Após calcular o Score de Sucesso, classificamos as músicas como:

- 🎧 **Hit** → Top 20% das músicas com maior score  
- 🎵 **Não Hit** → demais músicas  

Essa abordagem é baseada na distribuição dos dados, tornando o modelo mais robusto e adaptável.
""")

# =========================
# 📊 O QUE O USUÁRIO VAI VER
# =========================
st.header("📊 O que você vai encontrar")

st.markdown("""
Nas próximas páginas, você poderá explorar:

- 📊 Comparação entre hits e não-hits  
- 📈 Evolução da música ao longo dos anos  
- 🎯 Fatores que influenciam o sucesso  
- 🎧 Análise individual de artistas com dados reais do Spotify  

Use o menu lateral para navegar pelas análises.
""")

st.divider()

# =========================
# 🚀 FOOTER
# =========================
st.markdown("""
Projeto desenvolvido para análise de dados musicais utilizando Big Data e Machine Learning.
""")