import pandas as pd
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import plotly.express as px
import time
import os
from dotenv import load_dotenv

st.set_page_config(layout="wide")

# =========================
# 🎨 ESTILO PREMIUM (MELHORADO)
# =========================
st.markdown("""
<style>
body { background-color: #0e1117; color: #FAFAFA; }

.card {
    background-color: #181a20;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #2a2f3a;
    margin-bottom: 12px;
}

.small {
    color: #9ca3af;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🎧 HEADER
# =========================
col1, col2 = st.columns([1, 6])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg", width=70)
with col2:
    st.title("Spotify Analytics")
    st.caption("Exploração inteligente de artistas")

st.divider()

# =========================
# 🔐 ENV (PROFISSIONAL)
# =========================
load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

if not CLIENT_ID or not CLIENT_SECRET:
    st.warning("⚠️ Configure o .env com suas credenciais do Spotify")
    st.stop()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
))

# =========================
# 📂 DATASET
# =========================
@st.cache_data
def carregar_dados():
    df = pd.read_csv("dataset_musicas_com_nomes.csv")
    df["Artista"] = df["Artista"].astype(str).str.strip()
    return df

df = carregar_dados()

# =========================
# 🔍 BUSCA
# =========================
busca = st.text_input("🔍 Buscar artista")

artistas = sorted(df["Artista"].dropna().unique())

if busca:
    artistas = [a for a in artistas if busca.lower() in a.lower()]

artista = st.selectbox("🎤 Escolha um artista", artistas)

# =========================
# ⏳ LOADING
# =========================
with st.spinner("Carregando..."):
    time.sleep(0.8)

# =========================
# 🎤 API
# =========================
@st.cache_data
def buscar_artista(nome):
    try:
        r = sp.search(q=f'artist:"{nome}"', type="artist", limit=1)
        if r["artists"]["items"]:
            return r["artists"]["items"][0]
    except:
        return None

artista_info = buscar_artista(artista)

# =========================
# 🎤 PERFIL
# =========================
st.subheader("🎤 Perfil do artista")

col1, col2 = st.columns([1,2])

with col1:
    if artista_info and artista_info.get("images"):
        st.image(artista_info["images"][0]["url"], use_container_width=True)

with col2:
    if artista_info:
        seguidores = artista_info.get("followers", {}).get("total", 0)
        popularidade = artista_info.get("popularity", 0)

        c1, c2 = st.columns(2)
        c1.metric("👥 Seguidores", f"{seguidores:,}")
        c2.metric("🔥 Popularidade", popularidade)

st.divider()

# =========================
# 🎵 TOP TRACKS (VISUAL MELHOR)
# =========================
st.subheader("🎵 Principais músicas")

@st.cache_data
def top_tracks(artista_id):
    try:
        return sp.artist_top_tracks(artista_id, country="BR")["tracks"]
    except:
        return []

if artista_info:
    tracks = top_tracks(artista_info["id"])

    for t in tracks[:5]:

        col1, col2 = st.columns([1,3])

        with col1:
            if t["album"]["images"]:
                st.image(t["album"]["images"][0]["url"])

        with col2:
            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.markdown(f"**{t['name']}**")
            st.markdown(f'<div class="small">{t["album"]["name"]}</div>', unsafe_allow_html=True)

            st.markdown(
                f"""
                <iframe src="https://open.spotify.com/embed/track/{t['id']}"
                width="100%" height="80"></iframe>
                """,
                unsafe_allow_html=True
            )

            st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# =========================
# ⭐ RANKING (BONITO)
# =========================
st.subheader("⭐ Top músicas do dataset")

if "Popularidade" in df.columns:

    ranking = df.sort_values(by="Popularidade", ascending=False).head(5)

    for i, row in ranking.iterrows():
        st.markdown(f"""
        <div class="card">
        <b>#{list(ranking.index).index(i)+1} - {row['Nome_Musica']}</b><br>
        <span class="small">{row['Artista']}</span><br>
        Popularidade: {row['Popularidade']}
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =========================
# 🤖 RECOMENDAÇÃO (MELHORADA)
# =========================
st.subheader("🤖 Recomendações parecidas")

df_artista = df[df["Artista"] == artista]

metricas = ['Energia','Dancabilidade','Valencia']
metricas = [m for m in metricas if m in df.columns]

if len(metricas) >= 2 and not df_artista.empty:

    perfil = df_artista[metricas].mean()

    df_temp = df.copy()

    # remove o próprio artista
    df_temp = df_temp[df_temp["Artista"] != artista]

    df_temp['dist'] = df_temp[metricas].sub(perfil).abs().sum(axis=1)

    recomendadas = df_temp.sort_values("dist").head(5)

    for _, row in recomendadas.iterrows():
        st.markdown(f"""
        <div class="card">
        🎧 <b>{row['Nome_Musica']}</b><br>
        <span class="small">{row['Artista']}</span>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =========================
# 🎶 PLAYLIST
# =========================
st.subheader("🎶 Ouvir artista")

if artista_info:
    st.markdown(
        f"""
        <iframe src="https://open.spotify.com/embed/artist/{artista_info['id']}"
        width="100%" height="380"></iframe>
        """,
        unsafe_allow_html=True
    )