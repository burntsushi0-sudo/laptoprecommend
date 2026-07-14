import streamlit as st
from google import genai
import nh3
import time
import random

st.set_page_config(page_title="Laptop Jackpot", page_icon="🎰", layout="wide")

st.markdown("""
    <style>
    /* Dark Arcade Matrix Background */
    .stApp {
        background-color: #07090e;
        color: #00ffcc; 
        font-family: 'Courier New', Courier, monospace;
        background-image: radial-gradient(#1f1035 1px, transparent 0);
        background-size: 24px 24px;
    }
    
    /* CRT Scanline Overlay */
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: repeating-linear-gradient(0deg, rgba(0, 255, 204, 0.03), rgba(0, 255, 204, 0.03) 1px, transparent 1px, transparent 2px);
        pointer-events: none; z-index: 10;
    }

    h1, h2, h3 { color: #ffff00 !important; text-transform: uppercase; letter-spacing: 3px; text-shadow: 0 0 10px #ffff00;}
    p, span, label { color: #00ffcc !important; font-weight: bold; }

    /* Input Forms Matrix */
    .stNumberInput input, .stSelectbox select, .stSlider > div > div > div > div, .stTextArea textarea {
        background-color: #121620 !important;
        border: 2px solid #ff00ff !important;
        color: #00ffcc !important;
        border-radius: 4px;
        box-shadow: 0 0 10px #ff00ff, inset 0 0 5px #ff00ff;
    }

    /* The Main Lever / Spin Button */
    .stButton>button {
        background: linear-gradient(180deg, #ffff00, #ff00ff);
        color: #07090e !important;
        border: 3px solid #00ffcc !important;
        border-radius: 12px;
        text-transform: uppercase;
        width: 100%;
        padding: 20px;
        font-size: 24px !important;
        font-weight: 900 !important;
        transition: 0.2s ease-in-out;
        box-shadow: 0 0 20px #ff00ff, 0 0 40px #00ffcc;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px #ffff00, 0 0 50px #ff00ff;
    }

    /* Slot Machine Reel Enclosures */
    .slot-casing {
        background: linear-gradient(145deg, #18092b, #05020a) !important;
        border: 4px solid #ffff00 !important;
        border-radius: 16px;
        padding: 25px;
        box-shadow: 0 0 25px #ffff00, inset 0 0 15px #ff00ff;
        margin: 15px 0px;
        min-height: 450px;
        text-align: center;
    }
    
    .reel-header {
        background-color: #ff00ff;
        color: #07090e !important;
        font-weight: bold;
        padding: 5px;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 4px;
        margin-bottom: 20px;
        box-shadow: 0 0 10px #ff00ff;
    }

    /* Image Scaling inside the Slot Reel */
    img {
        border: 3px double #00ffcc;
        border-radius: 8px;
        box-shadow: 0 0 15px #00ffcc;
        margin: 15px auto;
        max-width: 100%;
        height: auto;
    }
    
    .slot-casing a {
        color: #ffff00 !important;
        text-decoration: underline;
    }
    </style>
""", unsafe_allow_html=True)


api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("🔑 ACCESS DENIED: INSERT COIN / INITIALIZE GEMINI_API_KEY.")
    st.stop()

client = genai.Client(api_key=api_key)


st.title("🎰 LAPTOP JACKPOT")
st.write("CRITICAL LINK: [ ESTABLISHED ] // CURRENCY: [ INR ] // PULL LEVER TO SPIN CORES")
st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    max_price = st.number_input("MAX_BUDGET LIMIT (₹ INR)", min_value=25000, max_value=500000, value=80000, step=5000)
    usage_type = st.selectbox(
        "WORKLOAD MATRIX PROFILE",
        ["General Multi-tasking (SYS_ADMIN)", "Software Development / compilation", "High-End Gaming & Streaming (AAA)", "4K Video / 3D Animation (RENDER)", "Media Consumption (CASUAL)"]
    )

with col2:
    os_choice = st.selectbox("TARGET RUNTIME OS", ["Windows 11 (Standard)", "macOS (Apple Ecosystem)", "Linux (Out-of-the-Box)", "ChromeOS (Cloud)", "No System Preference"])
    ram_target = st.select_slider("ALLOCATED RAM CAPACITY", options=["8GB", "16GB", "32GB", "64GB"], value="16GB")

custom_prompt = st.text_area(
    "ADDITIONAL SPECIFICATIONS & CONTEXT FIELDS",
    placeholder="e.g., 'Must have an accurate color profile display', 'No mechanical keyboard noise', 'Need multi-port arrays'"
)

st.markdown("---")


if st.button("🎰 PULL LEVER & SPIN SLOTS 🎰"):
    
    
    prompt = f"""
    You are an expert hardware architect and Indian electronics consumer analyst operating an arcade terminal network.
    Provide exactly 3 real-world laptop chassis models widely available in India matching these parameters:
    - Max Budget: ₹{max_price:,} INR
    - Profile: {usage_type}
    - OS Setup: {os_choice}
    - Base Memory Target: {ram_target}
    - Custom Parameters: {custom_prompt if custom_prompt.strip() else 'None'}
    
    OUTPUT FORMAT ARCHITECTURE:
    You must output your recommendations using a clean, easily split delimiter block. Use the tag `[SLOT_BREAK]` to separate your analysis for each laptop. 
    
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
    
    
    glitch_placeholders = st.columns(3)
    glitch_pool = [" [ CORE_SPINNING ] ", " [ 777_MATRIX ] ", " [ RENDER_LOCK ] ", " [ COMPILING... ] ", " [ PRICING_LOOP ] ", " [ TESLA_CORE ] ", " [ CHASSIS_SEEK ] "]
    
    
    for _ in range(12):
        for i in range(3):
            with glitch_placeholders[i]:
                st.markdown(f'<div class="slot-casing"><div class="reel-header">REEL {i+1}</div><h2 style="color:#ff00ff !important; padding-top:100px;">{random.choice(glitch_pool)}</h2></div>', unsafe_allow_html=True)
        time.sleep(0.12)
        
    
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )
        
        safe_output = nh3.clean(response.text)
        
    
        laptop_slots = [block.strip() for block in safe_output.split("[SLOT_BREAK]") if block.strip()]
        
        
        st.empty()
        st.balloons()
        st.success("🎰 JACKPOT! SYSTEM REELS SECURED:")
        
        final_reels = st.columns(3)
        
        
        for idx in range(min(len(laptop_slots), 3)):
            with final_reels[idx]:
                st.markdown(
                    f'<div class="slot-casing"><div class="reel-header">🎰 REEL {idx+1} MATED</div>{laptop_slots[idx]}</div>', 
                    unsafe_allow_html=True
                )
                
    except Exception as e:
        st.error(f"⚠️ SYSTEM_JAM: Mechanical issue in reel indexing array: {e}")
