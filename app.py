import streamlit as st

# Configurazione grafica per bambini
st.set_page_config(page_title="Missione Imparare", page_icon="🎨")

# Un tocco di colore con i CSS
st.markdown("""
    <style>
    .main { background-color: #E3F2FD; }
    .stButton>button { 
        background-color: #4CAF50; color: white; 
        border-radius: 20px; height: 3em; width: 100%;
        font-size: 20px; font-weight: bold;
    }
    h1 { color: #1E88E5; font-family: 'Comic Sans MS', cursive; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌟 La mia Bacheca Magica")

# Elenco alunni (puoi personalizzarlo)
alunni = ["Seleziona il tuo nome", "Alessandro", "Beatrice", "Chiara", "Davide", "Elena"]
nome = st.selectbox("Ciao! Chi sei oggi?", alunni)

if nome != "Seleziona il tuo nome":
    st.header(f"Ciao {nome}! 👋")
    
    st.header("🕵️ Missione: I Cacciatori di Articoli")

with st.expander("📖 Leggi il compito di oggi", expanded=True):
    st.write("""
    **Istruzioni:**
    Sul tuo quaderno, scrivi l'articolo determinativo giusto davanti a queste parole:
    - ... zaino
    - ... gatta
    - ... alberi
    - ... isola
    
    Poi scatta una foto e inviamela! 📸
    """)