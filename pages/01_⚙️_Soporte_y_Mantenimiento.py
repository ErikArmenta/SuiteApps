# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:21:04 2026

@author: acer
"""

import streamlit as st

st.set_page_config(page_title="Support & Maintenance", layout="wide")

st.title("🛠️ Support & Maintenance Catalog")

apps = [
    {"name": "Helium Calculator", "url": "https://heliumcalculete-eainnovation.streamlit.app/", "desc": "Specialized gas usage calculation."},
    {"name": "Excel Automator", "url": "https://automatizadorexcel.streamlit.app/", "desc": "Data processing and automation."},
    {"name": "Downtime Dashboard", "url": "https://dashboard-tiempo-muerto-soporteelectrico.streamlit.app/", "desc": "Electrical support metrics."},
    {"name": "2D Digital Twin", "url": "https://gemelodigital2d.streamlit.app/", "desc": "Visual representation of plant assets."},
    {"name": "Electric Support DCO", "url": "https://soporte-elec-dco.streamlit.app/", "desc": "Direct electrical maintenance control."},
    {"name": "Maintenance Dashboard", "url": "https://mantttodash-eainnovation.streamlit.app/", "desc": "Overall maintenance KPIs."},
    {"name": "Kanban System", "url": "https://sistemakanban-eainnovation.streamlit.app/", "desc": "Flow and task management."},
    {"name": "Sensor Management", "url": "https://sistemagestionsensores.streamlit.app/", "desc": "Industrial sensor tracking."}
]

# Grid de 3 columnas
cols = st.columns(3)
for i, app in enumerate(apps):
    with cols[i % 3]:
        st.info(f"**{app['name']}**")
        st.write(app['desc'])
        st.link_button("Open App", app['url'])