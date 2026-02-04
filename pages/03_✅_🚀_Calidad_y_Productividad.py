# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:26:47 2026

@author: acer
"""

import streamlit as st

st.set_page_config(page_title="Quality & Productivity", layout="wide")

st.markdown("""
    <style>
    .stAlert { background-color: #1e1e2e; border: 1px solid #10b981; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 Quality & Productivity Control")
st.write("Metrology, inspection systems, and real-time quality dashboards.")

apps_quality = [
    {
        "name": "Gage Track",
        "url": "https://gagetrack-eainnovation.streamlit.app/",
        "desc": "Metrology equipment calibration and tracking."
    },
    {
        "name": "QR System",
        "url": "https://qr-eainnovation.streamlit.app/",
        "desc": "Quick Response codes for industrial traceability."
    },
    {
        "name": "Quality Control Dashboard",
        "url": "https://qualitycontroldashboard-eainnovation.streamlit.app/",
        "desc": "Statistical Process Control (SPC) and real-time metrics."
    },
    {
        "name": "LPA Dashboard",
        "url": "https://software-lpa-dasboard.streamlit.app/",
        "desc": "Layered Process Audits management."
    },
    {
        "name": "Digital Gage",
        "url": "https://gagedigital-ea.streamlit.app/",
        "desc": "Advanced digital measurement interface."
    }
]

# Renderizado en columnas (2 filas de 3 y 2)
cols = st.columns(3)
for i, app in enumerate(apps_quality):
    with cols[i % 3]:
        st.success(f"### {app['name']}")
        st.write(app['desc'])
        st.link_button("Launch System", app['url'], use_container_width=True)

# Reemplazo de la línea con error por un separador visual y espacio
st.divider()
st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)

# Footer de la página (no fijo para que no estorbe el contenido)
st.caption("Developed by Master Engineer Erik Armenta | EA Innovation 2026")