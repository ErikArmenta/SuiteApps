# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:24:42 2026

@author: acer
"""

import streamlit as st

st.set_page_config(page_title="Manufacturing & Continuous Improvement", layout="wide")

# Estilo rápido para mantener consistencia
st.markdown("""
    <style>
    .stAlert { background-color: #1e293b; border: 1px solid #3b82f6; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏭 Manufacturing & Continuous Improvement")
st.write("Tools focused on operational excellence and process optimization.")

apps_mfg = [
    {
        "name": "5S & Continuous Improvement",
        "url": "https://mejoracontinua-5s-auditoria-eainnovation.streamlit.app/",
        "desc": "Audits and standard compliance tracking."
    },
    {
        "name": "Lab Studio",
        "url": "https://labstudio-eainnovation.streamlit.app/",
        "desc": "Experimental data analysis and laboratory management."
    },
    {
        "name": "BOM Reconciliation",
        "url": "https://bom-reconciliation-app-eainnovation.streamlit.app/",
        "desc": "Automated Bill of Materials comparison between SAP and Engineering."
    }
]

# Renderizado en columnas
cols = st.columns(3)
for i, app in enumerate(apps_mfg):
    with cols[i % 3]:
        st.info(f"### {app['name']}")
        st.write(app['desc'])
        st.link_button("Access Platform", app['url'], use_container_width=True)

# Reemplazo de la línea con error por un separador visual y espacio
st.divider()
st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)

# Footer de la página (no fijo para que no estorbe el contenido)
st.caption("Developed by Master Engineer Erik Armenta | EA Innovation 2026")