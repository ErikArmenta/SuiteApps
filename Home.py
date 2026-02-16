# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:18:38 2026

@author: acer
"""

import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="EA Innovation Suite", page_icon="🚀", layout="wide")

# --- 1.1 LÓGICA DE DATOS Y CALLBACKS ---
# Guardamos las apps en una lista para poder filtrarlas
todas_las_apps = [
    {"title": "Kanban System", "desc": "Real-time production tracking and flow control.", "url": "https://sistemakanban-eainnovation.streamlit.app/"},
    {"title": "Systems OEE", "desc": "Automated OEE real data base.", "url": "https://sistema-oee-ea.streamlit.app/"},
    {"title": "Digital Gage", "desc": "High-precision digital metrology and calibration tracking.", "url": "https://gagedigital-ea.streamlit.app/"},
]

def filtrar_suite_callback():
    query = st.session_state.buscador_suite.lower()
    st.session_state.apps_visibles = [
        app for app in todas_las_apps
        if query in app['title'].lower() or query in app['desc'].lower()
    ]

if 'apps_visibles' not in st.session_state:
    st.session_state.apps_visibles = todas_las_apps

# 2. Estilo CSS Avanzado (Mantenemos tu diseño original)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .app-card {
        background-color: #1f2937;
        border: 1px solid #374151;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 10px;
        transition: transform 0.3s ease, border-color 0.3s ease;
        text-align: center;
        height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .app-card:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
    }
    .app-title { color: #f3f4f6; font-size: 1.2rem; font-weight: bold; }
    .app-desc { color: #9ca3af; font-size: 0.9rem; }
    .footer {
        position: fixed; left: 0; bottom: 0; width: 100%;
        background-color: #0e1117; color: #6b7280;
        text-align: center; padding: 10px; font-size: 0.8rem;
        border-top: 1px solid #1f2937;
    }
    [data-testid="stMetricValue"] { font-size: 1.8rem; color: #3b82f6; }
    </style>
    """, unsafe_allow_html=True)

# 3. Header
col_header1, col_header2 = st.columns([1, 4])
with col_header1:
    st.image("EA_2.png", width=120)
with col_header2:
    st.title("EA Innovation - Engineering Suite")
    st.subheader("Industrial Applications Command Center")

st.divider()

# 4. Sección de Métricas
m1, m2, m3, m4 = st.columns(4)
m1.metric("Apps Desplegadas", "17", "Active")
m2.metric("Disponibilidad", "99.9%", "Stable")
m3.metric("Departamentos", "3", "Engineering")
m4.metric("Región", "Cd. Juárez", "MX")

st.divider()

# --- NUEVO: BUSCADOR CON CALLBACK ---
col_search1, col_search2 = st.columns([2, 1])
with col_search1:
    st.markdown("### 🛠️ Featured Applications")
with col_search2:
    st.text_input("🔍 Quick Launch:", key="buscador_suite", on_change=filtrar_suite_callback, placeholder="Search app...")

# 5. Renderizado de Cards (Usando la lista del callback)
cols = st.columns(3)
for i, app in enumerate(st.session_state.apps_visibles):
    with cols[i % 3]:
        st.markdown(f"""
            <div class="app-card">
                <div class="app-title">{app['title']}</div>
                <div class="app-desc">{app['desc']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button(f"Launch {app['title']}", app['url'], use_container_width=True)

st.divider()

# 7. --- SECCIÓN: ESTADO Y ROADMAP ---
col_status, col_roadmap = st.columns(2)

with col_status:
    st.markdown("### 🌐 System Status")
    st.write("✅ **Main Server:** Operational")
    st.write("✅ **Database (Google Sheets/Supabase):** Connected")
    st.write("✅ **Vision Engine (YOLO v10):** Online")
    st.info("Global Latency: 45ms")

with col_roadmap:
    st.markdown("### 🚀 Engineering Roadmap 2026")
    with st.expander("Ver Próximos Lanzamientos"):
        st.write("🔹 **Andon System:** Monitoreo con Supabase.")
        st.write("🔹 **Safety AI:** Detección de EPP con visión artificial.")
        st.write("🔹 **Mobile App:** Monitoreo de procesos en tiempo real.")

# 8. Sidebar y 9. Footer
st.sidebar.image("EA_2.png", use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.info("Support: Master Engineer Erik Armenta")

st.markdown(f"""
    <div class="footer">
        Developed by <b>Master Engineer Erik Armenta</b> | © 2026 EA Innovation | Industrial Engineering Solutions
    </div>
    """, unsafe_allow_html=True)


