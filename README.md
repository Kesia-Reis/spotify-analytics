# 🎧 Spotify Analytics

Projeto de análise de dados musicais com foco em entender **o que faz uma música se tornar um hit** na era do streaming.

---

## 📊 Sobre o Projeto

Com milhões de músicas lançadas todos os anos, identificar padrões de sucesso se tornou essencial.

Este projeto utiliza:

* 📈 Análise de dados
* 🎧 Integração com API do Spotify

para explorar e interpretar o comportamento de músicas de sucesso.

---

## 🎯 Objetivo

Responder à pergunta:

> **Quais fatores fazem uma música virar hit?**

---

## 🧠 Metodologia

Foi criado um **Score de Sucesso**, baseado em múltiplas variáveis:

* Streams (alcance)
* Crescimento (viralização)
* Replay (retenção)
* Skip (rejeição)
* Playlists (exposição)
* Compartilhamentos (engajamento)

### 📐 Fórmula do Score

```
Score = 0.25 * Streams +
        0.20 * Crescimento +
        0.15 * Replay +
        0.15 * (1 - Skip) +
        0.15 * Playlists +
        0.10 * Compartilhamentos
```

---

## 🏆 Classificação

* 🎧 **Hit** → Top 20% das músicas com maior score
* 🎵 **Não Hit** → restante

---

## 🚀 Funcionalidades

### 📊 Análise de Dados

* Comparação entre hits e não-hits
* Correlação de variáveis com sucesso
* Evolução das características musicais ao longo do tempo

### 🎤 Explorar Artistas

* Dados reais via API do Spotify
* Top músicas com player integrado
* Informações de popularidade e seguidores

### ⭐ Ranking

* Músicas mais populares do dataset

### 🔍 Recomendação Simples

Sistema baseado em **similaridade de características musicais**, considerando:

* Energia
* Dancabilidade
* Valencia

---

## 🖥️ Tecnologias

* Python
* Streamlit
* Pandas
* Plotly
* Spotipy (Spotify API)

---

## ▶️ Como rodar o projeto

### 1. Clonar repositório

```
git clone https://github.com/Kesia-Reis/spotify-analytics.git
```

### 2. Criar ambiente virtual

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

### 4. Configurar API do Spotify

Crie um arquivo `.env` na raiz:

```
SPOTIFY_CLIENT_ID=seu_client_id
SPOTIFY_CLIENT_SECRET=seu_client_secret
```

### 5. Rodar aplicação

```
streamlit run app.py
```

---

## 📚 Aprendizados

Durante o desenvolvimento, foram aplicados conceitos de:

* Análise exploratória de dados (EDA)
* Engenharia de métricas
* Integração com APIs externas
* Construção de dashboards interativos

---

## 👩‍💻 Autora

**Kesia Reis**

---

## 🚀 Futuras melhorias

* Aplicar modelos de Machine Learning
* Melhorar o sistema de recomendação
* Publicar aplicação online
