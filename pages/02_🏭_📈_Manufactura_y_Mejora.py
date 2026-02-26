# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:24:42 2026

@author: acer
"""

import streamlit as st

st.set_page_config(page_title="Manufacturing & Continuous Improvement", layout="wide")

# --- 1. LISTA DE DATOS ORIGINAL (CON NUEVA APP AÑADIDA) ---
apps_mfg = [
    {
        "name": "5S & Continuous Improvement",
        "url": "https://mejoracontinua-5s-auditoria-eainnovation.streamlit.app/",
        "form": "https://forms.gle/47KvPfGfoMakbzNt8",
        "desc": "Audits and standard compliance tracking."
    },
    {
        "name": "Lab Studio",
        "url": "https://labstudio-eainnovation.streamlit.app/",
        "form": None,
        "desc": "Experimental data analysis and laboratory management."
    },
    {
        "name": "BOM Reconciliation",
        "url": "https://bom-reconciliation-app-eainnovation.streamlit.app/",
        "form": None,
        "desc": "Automated Bill of Materials comparison between SAP and Engineering."
    },
    {
        "name": "Training Validation System",
        "url": "https://train-validation-ea-innovation.streamlit.app",
        "form": None,
        "desc": "Real-time operator competency verification and automated exception logging."
    }
]

# --- 2. LÓGICA DE CALLBACK (Sin borrar nada) ---
def filtrar_mfg_callback():
    # Buscamos en el nombre o en la descripción
    query = st.session_state.search_mfg.lower()
    st.session_state.mfg_filtrado = [
        app for app in apps_mfg 
        if query in app['name'].lower() or query in app['desc'].lower()
    ]

# Inicialización del estado de sesión
if 'mfg_filtrado' not in st.session_state:
    st.session_state.mfg_filtrado = apps_mfg

# --- 3. ESTILOS Y TÍTULOS ---
st.markdown("""
    <style>
    .stAlert { background-color: #1e293b; border: 1px solid #3b82f6; }
    div.stButton > button:first-child {
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏭 Manufacturing & Continuous Improvement")
st.write("Tools focused on operational excellence and process optimization.")

# Buscador con Callback
st.text_input(
    "🔍 Filtrar herramientas de mejora:", 
    key="search_mfg", 
    on_change=filtrar_mfg_callback,
    placeholder="Ej: '5S', 'BOM', 'SAP'..."
)

# --- 4. RENDERIZADO DINÁMICO ---
cols = st.columns(3)
# Iteramos sobre la lista filtrada por el callback
for i, app in enumerate(st.session_state.mfg_filtrado):
    with cols[i % 3]:
        with st.container(border=True):
            st.info(f"### {app['name']}")
            st.write(app['desc'])

            # Botón principal de la App
            st.link_button("🚀 Launch System", app['url'], use_container_width=True)

            # Botón de Formulario (Solo si existe en la lista)
            if app['form']:
                st.link_button("📝 Open 5S Audit Form", app['form'], use_container_width=True)
            else:
                st.write("")

# Separador y espacio final
st.divider()
st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)

# Footer
st.caption("Developed by Master Engineer Erik Armenta | EA Innovation 2026")



