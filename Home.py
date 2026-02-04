# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 10:18:38 2026

@author: acer
"""

import streamlit as st

# 1. Configuración de página
st.set_page_config(page_title="EA Innovation Suite", page_icon="🚀", layout="wide")

# 2. Estilo CSS Avanzado (Dark Mode & UI Moderna)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .app-card {
        background-color: #1f2937;
        border: 1px solid #374151;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.3s ease, border-color 0.3s ease;
        text-align: center;
        height: 250px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .app-card:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.5);
    }
    .app-title {
        color: #f3f4f6;
        font-size: 1.2rem;
        font-weight: bold;
    }
    .app-desc {
        color: #9ca3af;
        font-size: 0.9rem;
    }
    /* Estilo para los botones de la suite */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #3b82f6;
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #2563eb;
        border: none;
        color: white;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0e1117;
        color: #6b7280;
        text-align: center;
        padding: 10px;
        font-size: 0.8rem;
        border-top: 1px solid #1f2937;
    }
    /* Métrica personalizada */
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        color: #3b82f6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Header con Logo y Firma
col_header1, col_header2 = st.columns([1, 4])
with col_header1:
    st.image("EA_2.png", width=120)
with col_header2:
    st.title("EA Innovation - Engineering Suite")
    st.subheader("Industrial Applications Command Center")

st.divider()

# 4. Sección de Métricas de Impacto
m1, m2, m3, m4 = st.columns(4)
m1.metric("Apps Desplegadas", "16", "Active")
m2.metric("Disponibilidad", "99.9%", "Stable")
m3.metric("Departamentos", "3", "Engineering")
m4.metric("Región", "Cd. Juárez", "MX")

st.divider()

# 5. Función para renderizar Cards
def render_app_card(title, description, url):
    with st.container():
        st.markdown(f"""
            <div class="app-card">
                <div class="app-title">{title}</div>
                <div class="app-desc">{description}</div>
            </div>
        """, unsafe_allow_html=True)
        st.link_button(f"Launch {title}", url)

# 6. --- SECCIÓN: HIGHLIGHTS (Apps Destacadas) ---
st.markdown("### 🛠️ Featured Applications")
col_a, col_b, col_c = st.columns(3)

with col_a:
    render_app_card("Kanban System", "Real-time production tracking and flow control.", "https://sistemakanban-eainnovation.streamlit.app/")

with col_b:
    render_app_card("BOM Reconciliation", "Automated SAP vs Platform BOM comparison engine.", "https://bom-reconciliation-app-eainnovation.streamlit.app/")

with col_c:
    render_app_card("Digital Gage", "High-precision digital metrology and calibration tracking.", "https://gagedigital-ea.streamlit.app/")

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
        st.write("🔹 **Andon System:** Monitoreo de alertas en tiempo real con Supabase.")
        st.write("🔹 **Safety AI:** Detección de EPP (Cascos) mediante visión artificial.")
        st.write("🔹 **ONNX Integration:** Optimización de modelos para inferencia en milisegundos.")
        st.write("🔹 **Sistema de monitorieo de scrap.**")
        st.write("🔹 **Sistema de control de inventario toolcrip.**")
        st.write("🔹 **Aplicacion mobile de monitoreo de proecesos.**")

# 8. Sidebar Navigation Info
st.sidebar.image("EA_2.png", use_container_width=True)
st.sidebar.markdown("---")
st.sidebar.success("Navega entre departamentos usando el menú superior.")
st.sidebar.info("""
**Support:**
Master Engineer Erik Armenta
GitHub: @ErikArmenta
""")

# 9. Footer con tu firma
st.markdown(f"""
    <div class="footer">
        Developed by <b>Master Engineer Erik Armenta</b> | © 2026 EA Innovation | Industrial Engineering Solutions
    </div>
    """, unsafe_allow_html=True)