import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Konfigurasi halaman Streamlit layar penuh
st.set_page_config(
    page_title="CIVEDU - Platform Pembelajaran Civic Edupreneurship",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hilangkan padding, header, dan footer bawaan Streamlit agar UI CIVEDU tampil full-screen
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            width: 100vw !important;
            height: 100vh !important;
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Baca dan render file index.html
html_file = Path(__file__).parent / "index.html"

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")
    components.html(html_content, height=900, scrolling=True)
else:
    st.error("File index.html tidak ditemukan. Pastikan index.html berada satu folder dengan app.py.")