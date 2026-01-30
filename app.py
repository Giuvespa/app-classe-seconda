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
    
    # --- INIZIO OPZIONE B: SFIDE CASUALI ---
    st.subheader("🕵️ La tua Sfida di oggi")
    
    # Lista delle possibili sfide (puoi aggiungerne quante ne vuoi!)
    sfide = [
        "Scrivi l'articolo giusto per: **zaino, amica, alberi, gnomo**.",
        "Trova gli articoli per: **stivale, isola, campioni, zaini**.",
        "Metti l'articolo a: **scatola, imbuto, occhiali, scoiattolo**.",
        "Cerca l'articolo per: **aquilone, orologio, scarpe, specchio**."
    ]

    # Usiamo lo 'session_state' di Streamlit per far sì che la sfida non cambi 
    # ogni volta che il bambino carica la foto
    if 'sfida_corrente' not in st.session_state:
        st.session_state.sfida_corrente = sfide[0]

    if st.button("🎲 GENERA UNA NUOVA SFIDA"):
        import random
        st.session_state.sfida_corrente = random.choice(sfide)

    # Box colorato che mostra la sfida scelta
    st.markdown(f"""
    <div style="background-color: #fff3e0; padding: 20px; border-radius: 15px; border-left: 10px solid #ff9800;">
        <p style="font-size: 18px;">{st.session_state.sfida_corrente}</p>
    </div>
    """, unsafe_allow_html=True)
    # --- FINE OPZIONE B ---
    
    Poi scatta una foto e inviamela! 📸

    """)
