# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:21:04 2026

@author: acer
"""

import streamlit as st

st.set_page_config(page_title="Support & Maintenance", layout="wide")

# --- 1. LISTA DE DATOS (Actualizada con Energy Analyzer y Reporteo OEE) ---
apps = [
    {"name": "Energy Analyzer", "url": "https://energy-analyzer-eainnovation.streamlit.app", "form": None, "desc": "Industrial energy analyzer, extracting data from HOBO datalogger."},
    {"name": "Helium Calculator", "url": "https://heliumcalculete-eainnovation.streamlit.app/", "form": "https://forms.gle/5Km92vqXKLQxEfma6", "desc": "Specialized gas usage calculation."},
    {"name": "Excel Automator", "url": "https://automatizadorexcel.streamlit.app/", "form": None, "desc": "Data processing and automation."},
    {"name": "Downtime Dashboard", "url": "https://dashtiempomuerto-soporte-electrico.streamlit.app/", "form": None, "desc": "Electrical support metrics."},
    {"name": "Electric Support DCO", "url": "https://soporte-elec-dco.streamlit.app/", "form": "https://forms.gle/Ro6f2aS7YPQw8dDa9", "desc": "Direct electrical maintenance control."},
    {"name": "Maintenance Dashboard", "url": "https://mantttodash-eainnovation.streamlit.app/", "form": "https://forms.gle/28RZ3jNgcAps21RN8", "desc": "Overall maintenance KPIs."},
    {"name": "Kanban System", "url": "https://sistemakanban-eainnovation.streamlit.app/", "form": None, "desc": "Flow and task management."},
    {"name": "Sensor Management", "url": "https://sistemagestionsensores.streamlit.app/", "form": None, "desc": "Industrial sensor tracking."},
    {"name": "Reporteo OEE", "url": "https://reporteoee.streamlit.app", "form": None, "desc": "Automated reporting with drill-down functionality for OEE analysis."}
]

# --- 2. LÓGICA DE CALLBACK ---
def filtrar_apps_callback():
    query = st.session_state.busqueda.lower()
    st.session_state.lista_filtrada = [
        app for app in apps
        if query in app['name'].lower() or query in app['desc'].lower()
    ]

if 'lista_filtrada' not in st.session_state:
    st.session_state.lista_filtrada = apps

# --- 3. INTERFAZ DE USUARIO ---
st.title("🛠️ Support & Maintenance Catalog")
st.write("Access industrial tools and data entry forms for maintenance operations.")

st.text_input(
    "🔍 Search System or Tool:",
    key="busqueda",
    on_change=filtrar_apps_callback,
    placeholder="Type 'Energy', 'Helium', 'DCO'..."
)

st.markdown("""
    <style>
    div.stButton > button:first-child {
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 4. RENDERIZADO ---
cols = st.columns(3)
for i, app in enumerate(st.session_state.lista_filtrada):
    with cols[i % 3]:
        with st.container(border=True):
            st.subheader(f"{app['name']}")
            st.write(app['desc'])

            st.link_button("🚀 Launch System", app['url'], use_container_width=True)

            if app['form']:
                st.link_button("📝 Open Data Form", app['form'], use_container_width=True)
            else:
                # Mantenemos el espacio para uniformidad visual
                st.write("")

st.divider()
st.caption("Developed by Master Engineer Erik Armenta | EA Innovation 2026")
