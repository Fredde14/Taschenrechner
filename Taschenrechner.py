import streamlit as st

# 1. Seitenkonfiguration für Smartphone-Ansicht
st.set_page_config(
    page_title="Playful Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Custom CSS für das "Playful-Professional" Smartphone-Layout
st.markdown(
    """
    <style>
    /* Streamlit Standard-Elemente verstecken für App-Look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hauptcontainer auf Smartphone-Breite begrenzen */
    .block-container {
        max-width: 400px;
        padding-top: 2rem;
        padding-bottom: 2rem;
        margin: auto;
    }
    
    /* Hintergrund der App mit lila Punkten (Polka Dot Pattern) */
    .stApp {
        background-color: #1e1830;
        background-image: radial-gradient(#624CAB 2px, transparent 2px);
        background-size: 24px 24px;
    }
    
    /* Styling für den PocketCalc-Titel (Helle, gut lesbare Farbe + Glow-Effekt) */
    .pocketcalc-title {
        text-align: center;
        color: #FFE58F;
        font-family: 'Trebuchet MS', 'Lucida Sans Unicode', 'Segoe UI', sans-serif;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: 0px;
        text-shadow: 0px 0px 10px rgba(255, 229, 143, 0.4);
    }
    
    /* Display-Design: Textfarbe explizit auf Weiß gesetzt */
    .stTextInput input {
        background-color: #3F3356 !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        font-size: 2.5rem !important;
        font-weight: bold;
        text-align: right;
        border-radius: 18px !important;
        border: 2px solid #624CAB !important;
        padding: 10px !important;
    }
    
    /* Button-Styling (Sanft stark abgerundet) */
    div.stButton > button {
        width: 100%;
        height: 65px;
        font-size: 1.5rem;
        font-weight: bold;
        border-radius: 25px;
        border: none;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        transition: all 0.1s ease;
    }
    
    div.stButton > button:hover {
        transform: scale(0.96);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Session State für den Rechner-Zustand initialisieren
if "expression" not in st.session_state:
    st.session_state.expression = ""

# 4. App Header mit hellem Titel und Emojis
st.markdown(
    "<h2 class='pocketcalc-title'>✨ 🧮 PocketCalc 🧮 ✨</h2>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #D4C5E2; font-size: 0.9rem; margin-bottom: 20px;'>Einfach. Verspielt. Überall dabei.</p>",
    unsafe_allow_html=True,
)


# Funktionen für die Logik
def add_to_expr(value):
    st.session_state.expression += str(value)


def clear_expr():
    st.session_state.expression = ""


def calculate():
    try:
        result = str(eval(st.session_state.expression))
        st.session_state.expression = result
    except ZeroDivisionError:
        st.session_state.expression = "Fehler (Div/0)"
    except Exception:
        st.session_state.expression = "Fehler"


# Display
display_val = st.session_state.expression if st.session_state.expression else "0"
st.text_input(
    "", value=display_val, label_visibility="collapsed", on_change=lambda: None
)

st.write("")  # kleiner Abstand

# 5. Tasten-Layout (Klassisches Raster: Zeile für Zeile)
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("C", use_container_width=True):
        clear_expr()
        st.rerun()
with col2:
    if st.button("(", use_container_width=True):
        add_to_expr("(")
        st.rerun()
with col3:
    if st.button(")", use_container_width=True):
        add_to_expr(")")
        st.rerun()
with col4:
    if st.button("÷", use_container_width=True):
        add_to_expr("/")
        st.rerun()

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("1", use_container_width=True):
        add_to_expr("1")
        st.rerun()
with col2:
    if st.button("2", use_container_width=True):
        add_to_expr("2")
        st.rerun()
with col3:
    if st.button("3", use_container_width=True):
        add_to_expr("3")
        st.rerun()
with col4:
    if st.button("×", use_container_width=True):
        add_to_expr("*")
        st.rerun()

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("4", use_container_width=True):
        add_to_expr("4")
        st.rerun()
with col2:
    if st.button("5", use_container_width=True):
        add_to_expr("5")
        st.rerun()
with col3:
    if st.button("6", use_container_width=True):
        add_to_expr("6")
        st.rerun()
with col4:
    if st.button("-", use_container_width=True):
        add_to_expr("-")
        st.rerun()

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("7", use_container_width=True):
        add_to_expr("7")
        st.rerun()
with col2:
    if st.button("8", use_container_width=True):
        add_to_expr("8")
        st.rerun()
with col3:
    if st.button("9", use_container_width=True):
        add_to_expr("9")
        st.rerun()
with col4:
    if st.button("+", use_container_width=True):
        add_to_expr("+")
        st.rerun()

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("0", use_container_width=True):
        add_to_expr("0")
        st.rerun()
with col2:
    if st.button(".", use_container_width=True):
        add_to_expr(".")
        st.rerun()
with col3:
    if st.button("⌫", use_container_width=True):
        st.session_state.expression = st.session_state.expression[:-1]
        st.rerun()
with col4:
    if st.button("=", use_container_width=True):
        calculate()
        st.rerun()
