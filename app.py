import streamlit as st
from google import genai
import nh3 

st.set_page_config(page_title="LAPTOP RECOMMENDER", page_icon="🖥️", layout="wide")

st.markdown("""
    <style>
    /* Dark Background & Retro Glow Matrix */
    .stApp {
        background-color: #0d1117;
        color: #00ffcc; 
        font-family: 'Courier New', Courier, monospace;
        background-image: linear-gradient(0deg, #0d1117 25%, #161b22 25%, #161b22 50%, #0d1117 50%, #0d1117 75%, #161b22 75%, #161b22 100%);
        background-size: 8px 8px;
    }
    
    /* Global Glow & CRT Scanlines */
    body { text-shadow: 0 0 5px #00ffcc; }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: repeating-linear-gradient(0deg, rgba(0, 255, 204, 0.05), rgba(0, 255, 204, 0.05) 1px, transparent 1px, transparent 2px);
        pointer-events: none; z-index: 10;
    }

    h1, h2, h3 { color: #ff00ff !important; text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 10px #ff00ff;}
    p, span, label { color: #00ffcc !important; }

    /* Input Fields & Dropdowns */
    .stNumberInput input, .stSelectbox select, .stSlider > div > div > div > div {
        background-color: #161b22 !important;
        border: 2px solid #00ffcc !important;
        color: #00ffcc !important;
        border-radius: 4px;
        box-shadow: 0 0 10px #00ffcc, inset 0 0 5px #00ffcc;
    }

    /* Primary Action Button */
    .stButton>button {
        background: linear-gradient(135deg, #0d1117, #00ffcc);
        color: #0d1117 !important;
        border: 2px solid #ff00ff !important;
        border-radius: 8px;
        text-transform: uppercase;
        width: 100%;
        transition: 0.3s ease-in-out;
        box-shadow: 0 0 15px #ff00ff, inset 0 0 10px #ff00ff;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0d1117, #ff00ff);
        box-shadow: 0 0 25px #ff00ff, inset 0 0 10px #ff00ff;
    }

    /* Terminal Console Box for Safe Output Rendering */
    .cyber-console {
        background-color: #0a0e14 !important;
        border: 2px dashed #30363d;
        padding: 20px;
        border-radius: 6px;
        box-shadow: inset 0 0 20px rgba(0, 255, 204, 0.1);
        margin-top: 20px;
    }
    
    img {
        border: 2px solid #ff00ff;
        border-radius: 6px;
        box-shadow: 0 0 10px #ff00ff;
        margin: 15px 0px;
        max-width: 400px;
    }
    </style>
""", unsafe_allow_html=True)

api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("🔑 Access Denied: GEMINI_API_KEY Missing. Run SYSTEM_REBOOT.")
    st.stop()

client = genai.Client(api_key=api_key)

st.title("🖥️ LAPTOP_RECOMMENDER")
st.write("SYS_STATUS: [ ONLINE ] // RETRO_SHIELD: [ NH3_ACTIVE ]")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    max_price = st.number_input("MAX_BUDGET Target (in ₹ INR)", min_value=25000, max_value=500000, value=80000, step=5000)
    usage_type = st.selectbox(
        "OPERATIONAL_USAGE Profile",
        ["General Multi-tasking (SYS_ADMIN)", "Software Development / compilation", "High-End Gaming & Streaming (AAA)", "4K Video / 3D Animation (RENDER)", "Media Consumption (CASUAL)"]
    )

with col2:
    os_choice = st.selectbox("TARGETED OS Environment", ["Windows 11 (Standard)", "macOS (Apple Ecosystem)", "Linux (Out-of-the-Box)", "ChromeOS (Cloud)", "No System Preference"])
    ram_target = st.select_slider("MINIMUM_REQUIRED RAM (SYS_MEMORY)", options=["8GB", "16GB", "32GB", "64GB"], value="16GB")

st.markdown("---")


if st.button("🚀 GENERATE CONFIG SPECTRUM"):
    
    prompt = f"""
    You are an expert laptop hardware engineer and Indian electronics market analyst operating within a cyberpunk console network.
    Recommend 3 real-world laptop models widely available in the Indian retail market right now matching these criteria:
    - Max Budget (INR): ₹{max_price:,}
    - Operational Usage: {usage_type}
    - Environment/OS: {os_choice}
    - Required Baseline RAM: {ram_target}
    
    CRITICAL OUTPUT REQUIREMENTS:
    1. For EACH laptop recommended, you MUST provide a visual representation using a standard Markdown image tag: `![Chassis Name](Image URL)`. Use clean, verified public images.
    2. Directly underneath the image, provide a clean, hyperlinked terminal text block: "[🔎 Click here to view live localized retail images on Google Search](https://www.google.com/search?q=laptop+name+india&tbm=isch)".
    3. All asset valuation pricing statements must be calculated in Indian Rupees (INR) utilizing the ₹ icon identifier.
    4. For each recommendation, map out the comprehensive hardware upgrade matrix (CPU, RAM, Storage, GPU).
    """
    
    with st.spinner("🧠 Initializing neural network array... Running sanitization firewalls..."):
        try:
            response = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=prompt
            )
            
            safe_ai_output = nh3.clean(response.text)
            
            st.success("🤖 ANALYSIS_COMPLETE! Output verified safe via firewalls:")
            
            st.markdown(f'<div class="cyber-console">{safe_ai_output}</div>', unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"⚠️ SYSTEM_EXCEPTION during API Link-up: {e}")