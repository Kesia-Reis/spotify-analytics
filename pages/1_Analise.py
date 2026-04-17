import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# =========================
# 🎨 ESTILO PROFISSIONAL
# =========================
st.markdown("""
<style>
body { background-color: #0e1117; color: white; }

.big-number {
    font-size: 48px;
    font-weight: bold;
    color: #1DB954;
}

.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 📂 DADOS
# =========================
@st.cache_data
def carregar():
    return pd.read_csv("dataset_musicas_com_nomes.csv")

df = carregar()

# =========================
# 🧠 SCORE
# =========================
if 'Score_Sucesso' not in df.columns:

    score = 0

    if 'Streams' in df.columns:
        score += 0.3 * df['Streams']

    if 'Taxa_Replay' in df.columns:
        score += 0.3 * df['Taxa_Replay']

    if 'Taxa_Skip' in df.columns:
        score += 0.2 * (1 - df['Taxa_Skip'])

    if 'Dancabilidade' in df.columns:
        score += 0.2 * df['Dancabilidade']

    df['Score_Sucesso'] = score

limite = df['Score_Sucesso'].quantile(0.8)

df['Categoria'] = df['Score_Sucesso'].apply(
    lambda x: 'Hit' if x >= limite else 'Não Hit'
)

# =========================
# 🎯 HEADER
# =========================
st.title("🎧 O segredo dos Hits")

st.markdown("### Descobrindo padrões de sucesso musical com dados")

# =========================
# 🧾 KPI PRINCIPAL
# =========================
hits = (df['Categoria'] == 'Hit').sum()
total = len(df)
taxa = hits / total

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🔥 Taxa de sucesso")
    st.markdown(f'<div class="big-number">{taxa*100:.1f}%</div>', unsafe_allow_html=True)
    st.caption("Apenas uma pequena parte das músicas vira hit")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🎵 Total analisado")
    st.markdown(f'<div class="big-number">{total}</div>', unsafe_allow_html=True)
    st.caption("Base de dados analisada")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# =========================
# 🧠 INSIGHT AUTOMÁTICO
# =========================
st.subheader("🧠 O que realmente importa")

corr = df.corr(numeric_only=True)

if 'Score_Sucesso' in corr.columns:

    corr = corr['Score_Sucesso'].drop('Score_Sucesso')
    corr = corr.sort_values(ascending=False)

    top1 = corr.index[0]
    top2 = corr.index[1]

    st.success(f"👉 As variáveis mais importantes são **{top1}** e **{top2}**")

    df_corr = pd.DataFrame({
        "Fator": corr.index,
        "Impacto": corr.values
    })

    fig = px.bar(
        df_corr.head(6),
        x="Impacto",
        y="Fator",
        orientation="h",
        color="Impacto",
        color_continuous_scale="greens"
    )

    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# =========================
# ⚔️ DIFERENÇA REAL
# =========================
st.subheader("⚔️ O que muda em um Hit")

metricas = ['Energia','Dancabilidade','Taxa_Replay','Taxa_Skip']
metricas = [m for m in metricas if m in df.columns]

if metricas:

    hit = df[df['Categoria'] == 'Hit'][metricas].mean()
    nao = df[df['Categoria'] == 'Não Hit'][metricas].mean()

    diff = (hit - nao).sort_values()

    df_diff = pd.DataFrame({
        "Métrica": diff.index,
        "Diferença": diff.values
    })

    fig2 = px.bar(
        df_diff,
        x="Diferença",
        y="Métrica",
        orientation="h",
        color="Diferença",
        color_continuous_scale=["red", "green"]
    )

    st.plotly_chart(fig2, use_container_width=True)

    melhor = diff.idxmax()

    st.info(f"🎯 O maior diferencial de um Hit é: **{melhor}**")

st.divider()

# =========================
# 🔥 TOP (ESTILO SPOTIFY)
# =========================
st.subheader("🔥 Top músicas")

if "Popularidade" in df.columns:

    top = df.sort_values(by="Popularidade", ascending=False).head(5)

    for i, row in top.iterrows():
        st.markdown(f"""
        <div class="card">
        <b>#{list(top.index).index(i)+1} - {row.get('Nome_Musica','')}</b><br>
        Popularidade: {row.get('Popularidade','')}
        </div>
        """, unsafe_allow_html=True)

st.divider()

# =========================
# 🔮 SIMULADOR INTELIGENTE
# =========================
st.subheader("🔮 Simulador de Hit")

col1, col2 = st.columns(2)

energia = col1.slider("Energia", 0.0, 1.0, 0.5)
dancabilidade = col1.slider("Dancabilidade", 0.0, 1.0, 0.5)
replay = col2.slider("Replay", 0.0, 1.0, 0.5)
skip = col2.slider("Skip", 0.0, 1.0, 0.5)

score = (
    0.3 * energia +
    0.3 * dancabilidade +
    0.3 * replay +
    0.1 * (1 - skip)
)

st.progress(score)

if score > 0.7:
    st.success("🔥 Forte candidato a HIT")
elif score > 0.5:
    st.warning("⚠️ Pode performar bem")
else:
    st.error("❌ Baixa chance")