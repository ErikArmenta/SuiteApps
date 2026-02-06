# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:26:47 2026

@author: acer
"""

import streamlit as st

st.set_page_config(page_title="Quality & Productivity", layout="wide")

# Estilo para mantener consistencia y espaciado de botones
st.markdown("""
    <style>
    .stAlert { background-color: #1e1e2e; border: 1px solid #10b981; }
    div.stButton > button {
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 Quality & Productivity Control")
st.write("Metrology, inspection systems, and real-time quality dashboards.")

# Lista de apps con soporte para múltiples formularios
apps_quality = [
    {
        "name": "Gage Track",
        "url": "https://gagetrack-eainnovation.streamlit.app/",
        "desc": "Metrology equipment calibration and tracking.",
        "forms": []
    },
    {
        "name": "QR System",
        "url": "https://qr-eainnovation.streamlit.app/",
        "desc": "Quick Response codes for industrial traceability.",
        "forms": []
    },
    {
        "name": "Quality Control Dashboard",
        "url": "https://qualitycontroldashboard-eainnovation.streamlit.app/",
        "desc": "Statistical Process Control (SPC) and real-time metrics.",
        "forms": []
    },
    {
        "name": "LPA Dashboard",
        "url": "https://software-lpa-dasboard.streamlit.app/",
        "desc": "Layered Process Audits management.",
        "forms": [
            {"label": "📝 Check List Nivel 1", "url": "https://forms.gle/imceoksCNGdy77d28"},
            {"label": "📝 Check List Nivel 2", "url": "https://forms.gle/7FZdWehvF8Uf6rwD9"}
        ]
    },
    {
        "name": "Digital Gage",
        "url": "https://gagedigital-ea.streamlit.app/",
        "desc": "Advanced digital measurement interface.",
        "forms": []
    }
]

# Renderizado en columnas (Grid de 3)
cols = st.columns(3)
for i, app in enumerate(apps_quality):
    with cols[i % 3]:
        with st.container(border=True):
            st.success(f"### {app['name']}")
            st.write(app['desc'])

            # Botón principal de la App
            st.link_button("🚀 Launch System", app['url'], use_container_width=True)

            # Renderizado dinámico de múltiples formularios si existen
            if app['forms']:
                for form in app['forms']:
                    st.link_button(form['label'], form['url'], use_container_width=True)
            else:
                st.write("") # Espacio para mantener alineación

# Espaciador visual
st.divider()
st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)

# Footer de la página
st.caption("Developed by Master Engineer Erik Armenta | EA Innovation 2026")
