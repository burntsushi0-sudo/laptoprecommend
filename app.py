import streamlit as st
from google import genai
import nh3
import time
import random


st.set_page_config(page_title="MATRIX CORE CONFIGURATOR", page_icon="📟", layout="wide")

st.markdown("""
    <style>
    /* Monochrome Green Phosphor / Matrix Core Background */
    .stApp {
        background-color: #000000;
        color: #00ff00; 
        font-family: 'Courier New', Courier, monospace;
        background-image: linear-gradient(0deg, rgba(0, 30, 0, 0.5) 50%, rgba(0, 0, 0, 1) 50%);
        background-size: 100% 4px; /* Simulates terminal hardware scanlines */
    }
    
    /* Terminal Cathode Glow and Grid */
    body {
        text-shadow: 0 0 4px #00ff00;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle, transparent 40%, rgba(0,0,0,0.4) 100%);
        pointer-events: none; z-index: 10;
    }

    h1, h2, h3 { color: #00ff00 !important; text-transform: uppercase; letter-spacing: 3px; text-shadow: 0 0 8px #00ff00;}
    p, span, label { color: #00cc00 !important; font-weight: bold; }

    /* Input Fields, Dropdowns & Custom Textareas: Cold Terminal Style */
    .stNumberInput input, .stSelectbox select, .stSlider > div > div > div > div, .stTextArea textarea {
        background-color: #050a05 !important;
        border: 2px solid #00ff00 !important;
        color: #00ff00 !important;
        border-radius: 2px;
        box-shadow: 0 0 8px #005500, inset 0 0 4px #003300;
        font-family: 'Courier New', Courier, monospace;
    }
    
    .stNumberInput input:focus, .stSelectbox select:focus, .stTextArea textarea:focus {
        border-color: #80ff80 !important;
        box-shadow: 0 0 12px #00ff00, inset 0 0 4px #005500;
    }

    /* The Main Override Interceptor Command Button */
    .stButton>button {
        background: linear-gradient(180deg, #003300, #001100);
        color: #00ff00 !important;
        border: 2px solid #00ff00 !important;
        border-radius: 4px;
        text-transform: uppercase;
        width: 100%;
        padding: 18px;
        font-size: 20px !important;
        font-weight: bold !important;
        transition: 0.2s ease-in-out;
        box-shadow: 0 0 12px #004400;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button:hover {
        background: #00ff00 !important;
        color: #000000 !important;
        box-shadow: 0 0 25px #00ff00;
        transform: scale(1.01);
    }

    /* Decryption Construct Core Modules */
    .slot-casing {
        background: #020502 !important;
        border: 2px solid #00ff00 !important;
        border-radius: 4px;
        padding: 25px;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.2), inset 0 0 10px rgba(0, 255, 0, 0.1);
        margin: 15px 0px;
        min-height: 520px;
        text-align: center;
        overflow: hidden;
        position: relative;
    }
    
    .reel-header {
        background-color: #00ff00;
        color: #000000 !important;
        font-weight: bold;
        padding: 6px;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 2px;
        margin-bottom: 20px;
        box-shadow: 0 0 8px #00ff00;
    }

    /* ⏳ DIGITAL RAIN STREAM ANIMATION KEYFRAMES ⏳ */
    @keyframes matrixStream {
        0% { transform: translateY(-20px); filter: blur(0px); opacity: 0.8; }
        50% { filter: blur(4px); opacity: 0.4; }
        100% { transform: translateY(60px); filter: blur(0px); opacity: 0.8; }
    }
    
    .spinning-content {
        animation: matrixStream 0.15s linear infinite;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-top: 40px;
        color: #00ff00 !important;
    }

    /* Decrypted Asset Core Formatting */
    img {
        border: 2px solid #00cc00;
        border-radius: 2px;
        box-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
        margin: 15px auto;
        max-width: 100%;
        height: auto;
        filter: grayscale(40%) contrast(120%);
    }
    
    .slot-casing a {
        color: #80ff80 !important;
        text-decoration: underline;
        text-shadow: 0 0 2px #00ff00;
    }
    </style>
""", unsafe_allow_html=True)


api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("🔑 ACCESS DENIED: SYSTEM CORES LOCKED. INITIALIZE GEMINI_API_KEY ENVIROMENT.")
    st.stop()

client = genai.Client(api_key=api_key)


st.title("📟 THE MATRIX: CONSTRUCT DECRYPTER")
st.write("SYS_STATUS: [ OPERATIONAL ] // CONNECTION: [ SECURE OVERRIDE ] // REGION: [ INR_MARKET ]")
st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    max_price = st.number_input("BUDGET CAP PARAMETER (₹ INR)", min_value=25000, max_value=500000, value=80000, step=5000)
    usage_type = st.selectbox(
        "WORKLOAD MATRIX PROFILE",
        ["General Multi-tasking (SYS_ADMIN)", "Software Development / compilation", "High-End Gaming & Streaming (AAA)", "4K Video / 3D Animation (RENDER)", "Media Consumption (CASUAL)"]
    )

with col2:
    os_choice = st.selectbox("TARGET RUNTIME OS", ["Windows 11 (Standard)", "macOS (Apple Ecosystem)", "Linux (Out-of-the-Box)", "ChromeOS (Cloud)", "No System Preference"])
    ram_target = st.select_slider("ALLOCATED RAM MATRIX CAPACITY", options=["8GB", "16GB", "32GB", "64GB"], value="16GB")

custom_prompt = st.text_area(
    "QUALITATIVE USER SPECIFICATIONS (DEEP CONTEXT INTERCEPT)",
    placeholder="e.g., 'Targeting localized compilation clusters', 'Need exact color parameters for matrix rendering', 'Must support multi-monitor layouts without thermal throttling'"
)

st.markdown("---")


if st.button("⚡ EXTRICATE RAW CONSTRUCT (DECRYPT) ⚡"):
    
    prompt = f"""
    You are the Lead Systems Architect of the Zion mainframe network decoding encrypted real-world hardware data.
    Provide exactly 3 real-world laptop chassis models widely available in the Indian retail market matching these metrics:
    - Max Budget: ₹{max_price:,} INR
    - Profile: {usage_type}
    - OS Setup: {os_choice}
    - Base Memory Target: {ram_target}
    - Custom Parameters: {custom_prompt if custom_prompt.strip() else 'None'}
    
    OUTPUT FORMAT ARCHITECTURE:
    You must output your recommendations using a clean, easily split delimiter block. Use the tag `[SLOT_BREAK]` to separate your analysis for each laptop core.
    
    For each of the 3 laptops, structure your response text as follows:
    ### Laptop Model Name
    `![Chassis Image](Clean Public Image URL)`
    [🔎 Localized Retail Target](https://www.google.com/search?q=laptop+name+india&tbm=isch)
    
    **Hardware Base Configuration Matrix:**
    - Value Estimation: ₹[Price in INR]
    - Core Configurations: [Details]
    - Expansion Upgrades: [Alternative configurations available in India]
    - Analytical Verdict: [Why this fits their workflow specs]
    """
    
    
    reels_placeholder = st.empty()
    
    
    with reels_placeholder.container():
        glitch_cols = st.columns(3)
        
        matrix_glyphs = ["1010", "ｦｱｳ", "ｼｵﾒ", "0110", "🔋📟", "🖳⚙️", "777"]
        for i in range(3):
            random_stream = f"{random.choice(matrix_glyphs)}\n{random.choice(matrix_glyphs)}\n{random.choice(matrix_glyphs)}"
            with glitch_cols[i]:
                st.markdown(f"""
                    <div class="slot-casing">
                        <div class="reel-header">STREAM {i+1} RUNNING</div>
                        <div class="spinning-content">
                            <h2 style="color:#00ff00 !important; font-size: 32px; white-space: pre-line;">{random_stream}</h2>
                            <h4 style="color:#80ff80 !important;">[ DECODING_DATASTREAM ]</h4>
                            <h2 style="color:#00ff00 !important; font-size: 32px; white-space: pre-line;">{random_stream[::-1]}</h2>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
    
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )
        
        safe_output = nh3.clean(response.text)
        laptop_slots = [block.strip() for block in safe_output.split("[SLOT_BREAK]") if block.strip()]
        
        
        time.sleep(1.0)
        
        
        reels_placeholder.empty()
        st.toast("🔓 DECRYPTION CORE MATRIX LOADED SUCCESSFULLY.")
        st.success("📟 SIGNAL SECURED. DECRYPTED CONSTRUCT OBJECTS MOUNTED:")
        
        final_reels = st.columns(3)
        for idx in range(min(len(laptop_slots), 3)):
            with final_reels[idx]:
                st.markdown(
                    f'<div class="slot-casing"><div class="reel-header">📟 CORE {idx+1} LOCKED</div>{laptop_slots[idx]}</div>', 
                    unsafe_allow_html=True
                )
                
    except Exception as e:
        reels_placeholder.empty()
        st.error(f"⚠️ COMPILATION_INTERRUPT: Core extraction sequence fractured: {e}")