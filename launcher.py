import streamlit as st

# Page configuration
st.set_page_config(
    page_title="CognitiveCloud.ai Math Apps",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    .app-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem;
        text-align: center;
        color: white;
        text-decoration: none;
        transition: transform 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .app-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    .app-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .app-title {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .app-description {
        font-size: 0.9rem;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🧠 CognitiveCloud.ai App Launcher</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Explore Xavier Honablue\'s interactive math apps - Choose your mathematical adventure!</p>', unsafe_allow_html=True)

# App data with descriptions and direct links
apps = [
    {
        "name": "📐 Algebra Rules",
        "description": "Master algebraic concepts and rules",
        "url": "https://algebra1rules-main-algebra1rulespy.streamlit.app/",
        "icon": "📐",
        "color": "#FF6B6B"
    },
    {
        "name": "📊 Calculus",
        "description": "Explore derivatives, integrals, and limits",
        "url": "https://calculus-main-apppy.streamlit.app/",
        "icon": "📊",
        "color": "#4ECDC4"
    },
    {
        "name": "🔴 Conic Sections",
        "description": "Visualize circles, ellipses, parabolas & hyperbolas",
        "url": "https://conicsections-main-apppy.streamlit.app/",
        "icon": "🔴",
        "color": "#45B7D1"
    },
    {
        "name": "🔢 Discrete Structures",
        "description": "Logic, sets, and combinatorics",
        "url": "https://discretestructures-main-apppy.streamlit.app/",
        "icon": "🔢",
        "color": "#96CEB4"
    },
    {
        "name": "📈 Distribution Curves",
        "description": "Statistical distributions and probability",
        "url": "https://distributioncurves-main-apppy.streamlit.app/",
        "icon": "📈",
        "color": "#FFEAA7"
    },
    {
        "name": "🍕 Fractions (Pizza Cutter)",
        "description": "Learn fractions with interactive pizza slices",
        "url": "https://fractions-main-pizzacutterpy.streamlit.app/",
        "icon": "🍕",
        "color": "#DDA0DD"
    },
    {
        "name": "🧠 Growth Mindset",
        "description": "Develop mathematical thinking skills",
        "url": "https://growthmindset-main-apppy.streamlit.app/",
        "icon": "🧠",
        "color": "#98D8C8"
    },
    {
        "name": "⚡ Irrational Numbers",
        "description": "Explore pi, e, and other irrational numbers",
        "url": "https://irrationalnumbers-main-irrationalnumberspy.streamlit.app/",
        "icon": "⚡",
        "color": "#F7DC6F"
    },
    {
        "name": "🎮 MathCraft",
        "description": "Gamified mathematics learning experience",
        "url": "https://mathcraft-main-streamlitapppy.streamlit.app/",
        "icon": "🎮",
        "color": "#BB8FCE"
    }
]

# Create a grid layout
cols_per_row = 3
rows = [apps[i:i + cols_per_row] for i in range(0, len(apps), cols_per_row)]

for row in rows:
    cols = st.columns(len(row))
    for col, app in zip(cols, row):
        with col:
            # Create clickable app cards
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {app['color']}22 0%, {app['color']}44 100%);
                border: 2px solid {app['color']};
                padding: 1.5rem;
                border-radius: 15px;
                text-align: center;
                margin: 0.5rem 0;
                transition: all 0.3s ease;
            ">
                <div style="font-size: 3rem; margin-bottom: 1rem;">{app['icon']}</div>
                <h3 style="color: #333; margin-bottom: 0.5rem;">{app['name'].split(' ', 1)[1]}</h3>
                <p style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">{app['description']}</p>
                <a href="{app['url']}" target="_blank" style="
                    background: {app['color']};
                    color: white;
                    padding: 0.75rem 1.5rem;
                    border-radius: 25px;
                    text-decoration: none;
                    font-weight: bold;
                    transition: all 0.3s ease;
                    display: inline-block;
                ">Launch App</a>
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; margin-top: 2rem; color: #666;">
    <p>💡 <strong>Empowering Young Minds in STEAM</strong></p>
    <p>Innovative learning solutions for grades 4-12 | Created by Xavier Honablue</p>
</div>
""", unsafe_allow_html=True)

# Optional: Add a quick stats section
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("🎯 Total Apps", len(apps))
with col2:
    st.metric("👥 Grade Levels", "4-12")
with col3:
    st.metric("📚 Subject Areas", "9+")
