import streamlit as st
import pandas as pd
import os
from datetime import datetime
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
from io import BytesIO

print(os.listdir())
print(os.listdir("utils"))


# Configuración de la página
st.set_page_config(page_title="CVT Final Processes", layout="wide")
st.title("Master App CVT Final Processes")

# --- Inicializar estado ---
if 'files' not in st.session_state:
    st.session_state.files = {}
if 'section' not in st.session_state:
    st.session_state.section = 'upload'

# --- Definir archivos esperados ---
expected_files = {
    "OEE": {"keywords": ["SQLReport"], "format": ["xlsx"]},
    "Production": {"keywords": ["05 - Overview", "31 - Overview", "correctionQty", "recken", "vpk"], "format": ["xlsx", "xlsx", "csv"]},
    "Scrap": {"keywords": ["EXPORT", "correctionQty", "recken", "vpk"], "format": ["xls", "xlsx"]},
    "Paros": {"keywords": ["n2", "n3"], "format": ["txt"]},
    "Oil Tracking": {"keywords": ["Tracking Consumo de ATF"], "format": ["xls", "xlsx"]},
    "Negative": {"keywords": ["neg"], "format": ["xls", "xlsx"]}
}

# --- Sidebar ---
st.sidebar.title("Menu")
if st.sidebar.button("📂 Cargar Archivos"):
    st.session_state.section = "upload"

# Habilitar botones según archivos cargados
for section_name, info in expected_files.items():
    if any(k in st.session_state.files for k in info['keywords']):
        if st.sidebar.button(section_name):
            st.session_state.section = section_name
