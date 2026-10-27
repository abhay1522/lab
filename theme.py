"""
Cyberpunk / Dark Lab Glassmorphism theme for Streamlit.
Translucent glass UI, glowing neon accents, modern sans-serif fonts.
Call apply_theme() once near the top of app.py.
"""

import streamlit as st

THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Inter:wght@300;400;600;700&display=swap');

/* ---------- Global Page Styling ---------- */
.stApp {
    background-color: #0b0f19;
    background-image: 
        radial-gradient(at 0% 0%, rgba(0, 242, 254, 0.08) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(127, 0, 255, 0.08) 0px, transparent 50%),
        linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 30px 30px, 30px 30px;
}

/* ---------- Top Navbar Glow ---------- */
[data-testid="stHeader"] {
    background: rgba(11, 15, 25, 0.7);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(0, 242, 254, 0.2);
}

/* ---------- Main Container: Glassmorphic Panel ---------- */
.block-container {
    background: rgba(18, 24, 38, 0.65);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    padding: 2.5rem 3rem !important;
    margin-top: 1.5rem;
    margin-bottom: 2rem;
}

/* ---------- Typography & Headers ---------- */
.stApp p, .stApp label, .stApp li, .stApp input, .stApp textarea,
.stApp [data-testid="stMarkdownContainer"], .stApp [data-testid="stCaptionContainer"] {
    font-family: 'Inter', sans-serif !important;
    color: #cbd5e1;
    font-size: 1rem;
}

h1, h2, h3, h4, .main-title, .section-title {
    font-family: 'Inter', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: -0.02em;
}

h1, .main-title {
    background: linear-gradient(135deg, #00f2fe 0%, #4facfe 50%, #7f00ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.2rem !important;
    text-shadow: 0 0 25px rgba(0, 242, 254, 0.3);
}

h2 {
    color: #00f2fe !important;
    font-size: 1.5rem !important;
    border-bottom: 1px solid rgba(0, 242, 254, 0.2);
    padding-bottom: 6px;
}

h3 {
    color: #38bdf8 !important;
    font-size: 1.25rem !important;
}

h4 {
    color: #a78bfa !important;
    font-size: 1.05rem !important;
}

code, pre, .stApp code {
    font-family: 'Fira Code', monospace !important;
    background: rgba(15, 23, 42, 0.8) !important;
    border: 1px solid rgba(56, 189, 248, 0.2) !important;
    border-radius: 6px;
    color: #38bdf8 !important;
}

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] {
    background-color: rgba(11, 15, 25, 0.85);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(0, 242, 254, 0.15);
}

/* ---------- Custom Interactive Buttons ---------- */
.stButton > button, .stDownloadButton > button, [data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, rgba(0, 242, 254, 0.15), rgba(127, 0, 255, 0.15));
    color: #ffffff !important;
    border: 1px solid rgba(0, 242, 254, 0.4);
    border-radius: 8px;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    padding: 0.6rem 1.4rem;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.stButton > button:hover, .stDownloadButton > button:hover {
    background: linear-gradient(135deg, rgba(0, 242, 254, 0.35), rgba(127, 0, 255, 0.35));
    border-color: #00f2fe;
    box-shadow: 0 0 15px rgba(0, 242, 254, 0.4);
    transform: translateY(-2px);
}

.stButton > button p, .stDownloadButton > button p {
    color: #ffffff !important;
    font-weight: 600 !important;
}

/* ---------- Inputs & Controls ---------- */
.stTextInput input, .stTextArea textarea, .stNumberInput input {
    background: rgba(15, 23, 42, 0.7) !important;
    color: #f8fafc !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 8px !important;
    backdrop-filter: blur(4px);
}

.stTextInput input:focus, .stTextArea textarea:focus, .stNumberInput input:focus {
    border-color: #00f2fe !important;
    box-shadow: 0 0 10px rgba(0, 242, 254, 0.3) !important;
}

[data-baseweb="select"] > div {
    background: rgba(15, 23, 42, 0.7) !important;
    border: 1px solid rgba(255, 255, 255, 0.15) !important;
    border-radius: 8px !important;
}

/* ---------- Metrics Cards ---------- */
[data-testid="stMetric"] {
    background: rgba(30, 41, 59, 0.5);
    border: 1px solid rgba(56, 189, 248, 0.2);
    border-radius: 12px;
    padding: 16px 20px;
    backdrop-filter: blur(8px);
}

[data-testid="stMetricLabel"] {
    color: #94a3b8 !important;
    font-size: 0.85rem !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

[data-testid="stMetricValue"] {
    color: #00f2fe !important;
    font-family: 'Fira Code', monospace !important;
    font-size: 1.5rem !important;
}

/* ---------- Tabs & Dividers ---------- */
[data-baseweb="tab"] {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600;
}

hr {
    border: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0, 242, 254, 0.4), transparent);
    margin: 1.5rem 0;
}
</style>
"""


def apply_theme():
    """Inject the Cyberpunk Dark Lab theme into Streamlit."""
    st.markdown(THEME_CSS, unsafe_allow_html=True)
