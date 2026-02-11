# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:24:42 2026

@author: acer
"""

import streamlit as st

st.set_page_config(page_title="Manufacturing & Continuous Improvement", layout="wide")

# Estilo para mantener consistencia y espaciado de botones
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

# Lista de apps con soporte para formularios
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
        "name": "Systems OEE",
        "url": "https://sistema-oee-ea.streamlit.app/",
        "form": None,
        "desc": "Automated OEE real data base."
    }

]

# Renderizado en columnas con contenedores para un look profesional
cols = st.columns(3)
for i, app in enumerate(apps_mfg):
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
                # Mantener balance visual
                st.write("")

# Separador y espacio final
st.divider()
st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)

# Footer
st.caption("Developed by Master Engineer Erik Armenta | EA Innovation 2026")


