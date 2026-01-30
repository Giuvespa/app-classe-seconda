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
    
    # Sezione Esercizio del giorno
    with st.expander("📖 Leggi la missione di oggi", expanded=True):
        st.write("Scatta una foto chiara del tuo esercizio di italiano e caricala qui sotto!")
        # Esempio di audio istruzione (puoi caricare un tuo file .mp3)
        # st.audio("istruzioni.mp3") 

    # Caricamento file
    foto = st.file_uploader("Premi qui per caricare la foto", type=['png', 'jpg', 'jpeg'])

    if st.button("INVIA ALLA MAESTRA 🚀"):
        if foto is not None:
            # Simulazione salvataggio
            st.balloons()
            st.success(f"GRANDE {nome}! Compito inviato. Sei un campione! 🏆")
            
            # Qui inseriremo in futuro la funzione AI per analizzare la foto
        else:
            st.error("Ops! Non hai ancora selezionato la foto del quaderno.")