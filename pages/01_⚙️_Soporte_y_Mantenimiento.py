# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:21:04 2026

@author: acer
"""

import streamlit as st

st.set_page_config(page_title="Support & Maintenance", layout="wide")

st.title("🛠️ Support & Maintenance Catalog")
st.write("Access industrial tools and data entry forms for maintenance operations.")

# Lista de apps con sus respectivos formularios donde aplica
apps = [
    {
        "name": "Helium Calculator",
        "url": "https://heliumcalculete-eainnovation.streamlit.app/",
        "form": "https://forms.gle/5Km92vqXKLQxEfma6",
        "desc": "Specialized gas usage calculation."
    },
    {
        "name": "Excel Automator",
        "url": "https://automatizadorexcel.streamlit.app/",
        "form": None,
        "desc": "Data processing and automation."
    },
    {
        "name": "Downtime Dashboard",
        "url": "https://dashboard-tiempo-muerto-soporteelectrico.streamlit.app/",
        "form": None,
        "desc": "Electrical support metrics."
    },
    {
        "name": "2D Digital Twin",
        "url": "https://gemelodigital2d.streamlit.app/",
        "form": None,
        "desc": "Visual representation of plant assets."
    },
    {
        "name": "Electric Support DCO",
        "url": "https://soporte-elec-dco.streamlit.app/",
        "form": "https://forms.gle/Ro6f2aS7YPQw8dDa9",
        "desc": "Direct electrical maintenance control."
    },
    {
        "name": "Maintenance Dashboard",
        "url": "https://mantttodash-eainnovation.streamlit.app/",
        "form": "https://forms.gle/28RZ3jNgcAps21RN8",
        "desc": "Overall maintenance KPIs."
    },
    {
        "name": "Kanban System",
        "url": "https://sistemakanban-eainnovation.streamlit.app/",
        "form": None,
        "desc": "Flow and task management."
    },
    {
        "name": "Sensor Management",
        "url": "https://sistemagestionsensores.streamlit.app/",
        "form": None,
        "desc": "Industrial sensor tracking."
    }
]

# Estilo para botones de formulario (opcional para resaltar)
st.markdown("""
    <style>
    div.stButton > button:first-child {
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Grid de 3 columnas
cols = st.columns(3)
for i, app in enumerate(apps):
    with cols[i % 3]:
        with st.container(border=True): # Añadimos un borde para separar mejor las apps
            st.subheader(f"{app['name']}")
            st.write(app['desc'])

            # Botón de la App Principal
            st.link_button("🚀 Launch System", app['url'], use_container_width=True)

            # Botón del Formulario (Solo si existe)
            if app['form']:
                st.link_button("📝 Open Data Form", app['form'], use_container_width=True)
            else:
                # Espacio vacío para mantener la alineación si no hay formulario
                st.write("")

st.divider()
st.caption("Developed by Master Engineer Erik Armenta | EA Innovation 2026")

