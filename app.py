import streamlit as st
from google import genai
import textwrap

# 1. Fundamental Page Configuration & Advanced CSS Injection
st.set_page_config(page_title="Laptop Recommender", page_icon="🖥️", layout="wide")

# High-Level Visual Stylization Matrix
st.markdown("""
    <style>
    /* Dark Background & Retro Glow */
    .stApp {
        background-color: #0d1117;
        color: #00ffcc; /* Neon Cyan */
        font-family: 'Courier New', Courier, monospace;
        background-image: linear-gradient(0deg, #0d1117 25%, #161b22 25%, #161b22 50%, #0d1117 50%, #0d1117 75%, #161b22 75%, #161b22 100%);
        background-size: 8px 8px; /* subtle grid pattern */
    }
    
    /* Global Glow & Scanlines */
    body {
        text-shadow: 0 0 5px #00ffcc;
    }
    .stApp::before {
        content: "";
        position: absolute;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: repeating-linear-gradient(0deg, rgba(0, 255, 204, 0.1), rgba(0, 255, 204, 0.1) 1px, transparent 1px, transparent 2px);
        pointer-events: none;
        z-index: 10;
    }

    /* Style titles */
    h1, h2, h3 { color: #ff00ff !important; /* Neon Magenta */ text-transform: uppercase; letter-spacing: 2px; text-shadow: 0 0 10px #ff00ff;}
    p, span, label { color: #00ffcc !important; }

    /* Input Fields, Sliders, and Dropdowns: Neon Borders & Terminal Style */
    .stNumberInput input, .stSelectbox select, .stSlider > div > div > div > div {
        background-color: #161b22 !important;
        border: 2px solid #00ffcc !important;
        color: #00ffcc !important;
        border-radius: 4px;
        box-shadow: 0 0 10px #00ffcc, inset 0 0 5px #00ffcc;
        font-family: 'Courier New', Courier, monospace;
    }
    .stSlider > div > div > div > div:hover {
        border-color: #ff00ff !important;
        box-shadow: 0 0 15px #ff00ff, inset 0 0 5px #ff00ff;
    }

    /* Primary Action Button: The Cyber-Launch Command */
    .stButton>button {
        background: linear-gradient(135deg, #0d1117, #00ffcc);
        color: #0d1117 !important;
        border: 2px solid #ff00ff !important;
        border-radius: 8px;
        font-weight: bold;
        text-transform: uppercase;
        width: 100%;
        transition: 0.3s ease-in-out;
        box-shadow: 0 0 15px #ff00ff, inset 0 0 10px #ff00ff;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0d1117, #ff00ff);
        color: #0d1117 !important;
        box-shadow: 0 0 25px #ff00ff, inset 0 0 10px #ff00ff;
        transform: translateY(-2px) scale(1.02);
    }

    /* AI Output Area: Console Styling */
    .stMarkdown div {
        background-color: #0a0e14;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 4px;
        box-shadow: inset 0 0 10px rgba(0, 255, 204, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Secure API Authentication Check
api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("🔑 Access Denied: GEMINI_API_KEY Missing. Run SYSTEM_REBOOT.")
    st.stop()

client = genai.Client(api_key=api_key)

# 2. Main Terminal Header
st.title("🖥️ AI PRECISION CONFIGURATOR (INDIA)")
st.write("SYS_STATUS: [ ONLINE ] // MARKET_DATA: [ INR ] // AI_MODEL: [ GEMINI-3.5-FLASH ]")
st.write("Initializing secure hardware matching matrix...")
st.markdown("---")

# 3. Input Interface (Retro columns)
col1, col2 = st.columns(2)

with col1:
    # Price Input Component (INR scaling, neon border)
    max_price = st.number_input(
        "MAX_BUDGET Target (in ₹ INR)", 
        min_value=25000, 
        max_value=500000, 
        value=80000, 
        step=5000,
        help="Input numeric parameter (INR)"
    )
    
    # Usage Type Dropdown Selection
    usage_type = st.selectbox(
        "OPERATIONAL_USAGE Profile",
        [
            "General Multi-tasking (SYS_ADMIN)",
            "Software Development / compilation",
            "High-End Gaming & Streaming (AAA)",
            "4K Video / 3D Animation (RENDER)",
            "Media Consumption (CASUAL)"
        ]
    )

with col2:
    # Operating System Dropdown Choice
    os_choice = st.selectbox(
        "TARGETED OS Environment",
        ["Windows 11 (Standard)", "macOS (Apple Ecosystem)", "Linux (Out-of-the-Box)", "ChromeOS (Cloud)", "No System Preference"]
    )
    
    # Target RAM Slider Component
    ram_target = st.select_slider(
        "MINIMUM_REQUIRED RAM (SYS_MEMORY)",
        options=["8GB", "16GB", "32GB", "64GB"],
        value="16GB"
    )

st.markdown("---")

# 4. The Cyber-Launch Command
if st.button("🚀 GENERATE CONFIG SPECTRUM"):
    
    # Constructing a structured prompt out of user parameters, enforcing INR
    prompt = f"""
    You are an expert laptop hardware engineer and Indian consumer electronics market analyst.
    Act as an impartial AI advisor operating in a secure terminal. Recommend 3 current real-world laptop models Widely available in the Indian market that fit these exact parameters:
    
    [PARAMETER SET]
    - Max Budget (INR): ₹{max_price:,}
    - Operational Usage: {usage_type}
    - Environment/OS: {os_choice}
    - Required Baseline RAM: {ram_target}
    
    MANDATORY INSTRUCTIONS:
    1. Focus *exclusively* on models available through official channels or major retailers in India. All price references, variation costs, and retail estimates must be in Indian Rupees (INR) using the ₹ symbol. No USD equivalents.
    2. Format the response as a clear system console readout. Use bolding and structured lists.
    3. For each recommended machine chassis line, provide a dedicated sub-section mapping out the Full Spectrum of Possible Configuration alternatives:
        - CPU tiers (e.g., Core Ultra 5 vs Core Ultra 7)
        - Memory upgrades (e.g., if scalable to 32GB/64GB)
        - Storage variations (e.g., 512GB to 2TB SSD)
        - GPU variations (e.g., RTX 4050 vs RTX 4060 configurations)
    """
    
    with st.spinner("🧠 Scanning neural market matrices for INR benchmarks..."):
        try:
            # Using the fast, developer-tier Gemini 3.5 Flash model
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )
            
            st.success("🤖 ANALYSIS_COMPLETE! Outputting Configuration Matrix:")
            
            # Formats output text as standard console block
            formatted_text = textwrap.indent(response.text, ' > ')
            st.code(formatted_text, language='text')
            
        except Exception as e:
            st.error(f"⚠️ SYSTEM_EXCEPTION during API Link-up: {e}")