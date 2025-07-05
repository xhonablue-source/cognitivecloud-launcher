import streamlit as st

st.set_page_config(page_title="CognitiveCloud Launcher", layout="centered")

st.title("🌩️ CognitiveCloud.ai App Launcher")
st.markdown("Explore Xavier Honablue’s interactive math apps:")

apps = {
    "📐 Algebra Rules": "https://xhonablue-source-algebralules-main-algebralulespy.streamlit.app/",
    "📊 Calculus": "https://xhonablue-source-calculus-main-apppy.streamlit.app/",
    "🎯 Conic Sections": "https://xhonablue-source-conicsections-main-apppy.streamlit.app/",
    "🔢 Discrete Structures": "https://xhonablue-source-discretestructures-main-apppy.streamlit.app/",
    "📈 Distribution Curves": "https://xhonablue-source-distributioncurves-main-apppy.streamlit.app/",
    "🍕 Fractions (Pizza Cutter)": "https://xhonablue-source-fractions-main-pizza_cutterpy.streamlit.app/",
    "🧠 Growth Mindset": "https://xhonablue-source-growthmindset-main-apppy.streamlit.app/",
    "🔺 Irrational Numbers": "https://xhonablue-source-irrationalnumbers-main-irrationalnumberspy.streamlit.app/",
    "🧮 MathCraft": "https://xhonablue-source-mathcraft-main-streamlit_apppy.streamlit.app/"
}

for name, url in apps.items():
    st.markdown(f"[{name}]({url})")
