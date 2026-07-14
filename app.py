import streamlit as st
from google import genai
import nh3
import time
import random


st.set_page_config(page_title="OASIS RIG CONFIGURATOR", page_icon="🕹️", layout="wide")

st.markdown("""
    <style>
    /* Neon Synthwave / OASIS Core Background */
    .stApp {
        background-color: #0c051b;
        color: #00ffff; 
        font-family: 'Courier New', Courier, monospace;
        background-image: linear-gradient(0deg, rgba(255, 0, 128, 0.08) 50%, rgba(0, 0, 0, 1) 50%);
        background-size: 100% 4px; /* Simulates retro arcade scanlines */
    }
    
    /* Neon Glow Effect */
    body {
        text-shadow: 0 0 5px #00ffff;
    }
    .stApp::before {
        content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle, transparent 30%, rgba(12, 5, 27, 0.6) 100%);
        pointer-events: none; z-index: 10;
    }

    h1, h2, h3 { color: #ff007f !important; text-transform: uppercase; letter-spacing: 3px; text-shadow: 0 0 10px #ff007f;}
    p, span, label { color: #00ffff !important; font-weight: bold; }

    /* Input Fields, Dropdowns & Custom Textareas: Retro Cyberpunk Arcade Style */
    .stNumberInput input, .stSelectbox select, .stSlider > div > div > div > div, .stTextArea textarea {
        background-color: #160a29 !important;
        border: 2px solid #ff007f !important;
        color: #00ffff !important;
        border-radius: 4px;
        box-shadow: 0 0 8px #7f00ff, inset 0 0 4px #2b0054;
        font-family: 'Courier New', Courier, monospace;
    }
    
    .stNumberInput input:focus, .stSelectbox select:focus, .stTextArea textarea:focus {
        border-color: #00ffff !important;
        box-shadow: 0 0 15px #00ffff, inset 0 0 4px #007f7f;
    }

    /* The Main OASIS Login / Spawn Rig Command Button */
    .stButton>button {
        background: linear-gradient(180deg, #ff007f, #7f00ff);
        color: #ffffff !important;
        border: 2px solid #00ffff !important;
        border-radius: 6px;
        text-transform: uppercase;
        width: 100%;
        padding: 18px;
        font-size: 20px !important;
        font-weight: bold !important;
        transition: 0.2s ease-in-out;
        box-shadow: 0 0 15px #ff007f;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button:hover {
        background: #00ffff !important;
        color: #000000 !important;
        box-shadow: 0 0 30px #00ffff;
        transform: scale(1.01);
    }

    /* Gunter Inventory Slot Core Modules */
    .slot-casing {
        background: #120624 !important;
        border: 2px solid #00ffff !important;
        border-radius: 6px;
        padding: 25px;
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3), inset 0 0 10px rgba(127, 0, 255, 0.2);
        margin: 15px 0px;
        min-height: 560px;
        text-align: left;
        overflow: hidden;
        position: relative;
    }
    
    .reel-header {
        background-color: #ff007f;
        color: #ffffff !important;
        font-weight: bold;
        padding: 6px;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-radius: 3px;
        margin-bottom: 20px;
        box-shadow: 0 0 10px #ff007f;
        text-align: center;
    }

    /* ⏳ RETRO GLITCH PULSE ANIMATION KEYFRAMES ⏳ */
    @keyframes oasisPulse {
        0% { opacity: 0.7; transform: scale(0.98); filter: hue-rotate(0deg); }
        50% { opacity: 1; transform: scale(1.01); filter: hue-rotate(45deg); }
        100% { opacity: 0.7; transform: scale(0.98); filter: hue-rotate(0deg); }
    }
    
    .spinning-content {
        animation: oasisPulse 0.3s ease-in-out infinite;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-top: 40px;
        color: #ff007f !important;
    }

    /* Artifact Asset Core Formatting */
    .slot-casing img {
        border: 2px solid #ff007f;
        border-radius: 4px;
        box-shadow: 0 0 12px rgba(255, 0, 127, 0.5);
        margin: 15px auto;
        display: block;
        max-width: 100%;
        height: auto;
        filter: saturate(130%) contrast(110%);
    }
    
    .slot-casing a {
        color: #00ffff !important;
        text-decoration: none !important;
        border: 1px solid #00ffff;
        padding: 5px 10px;
        border-radius: 4px;
        text-shadow: 0 0 6px #00ffff;
        font-weight: bold;
        display: block;
        text-align: center;
        margin: 10px 0px;
        background: rgba(0, 255, 255, 0.1);
    }
    .slot-casing a:hover {
        background: #00ffff !important;
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("🔑 REGISTRATION FAILED: OASIS TERMINAL LOCKED. INITIALIZE GEMINI_API_KEY ENVIRONMENT.")
    st.stop()

client = genai.Client(api_key=api_key)


st.title("🕹️ THE OASIS: RIG SLOT MACHINE")
st.write("PLAYER_STATUS: [ READY ] // LINK: [ ANORAK'S ALMANAC DECRYPTOR ] // MARKET: [ INR_REGION ]")
st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    max_price = st.number_input("COIN INVENTORY BUDGET (₹ INR)", min_value=25000, max_value=500000, value=80000, step=5000)
    usage_type = st.selectbox(
        "AVATAR CLASS & QUEST PROFILE",
        ["Computer Science Engneering Rig", "Electronics and Communication Rig", "Casual Rig(Browsing rig)", "Mechanical Engineering rig", "Gaming rig"]
    )

with col2:
    os_choice = st.selectbox("OPERATING SYSTEM HAPTIKS", ["Windows 11 (Standard)", "macOS (Apple Ecosystem)", "Linux (Out-of-the-Box)", "ChromeOS (Cloud)", "No System Preference"])
    ram_target = st.select_slider("MEMORY BUFFER MATRIX (RAM)", options=["8GB", "16GB", "32GB", "64GB"], value="16GB")

custom_prompt = st.text_area(
    "ANORAK'S ALMANAC ADDITIONAL CLUES (CUSTOM RIG SPECS)",
    placeholder="e.g., 'Must support dual-booting for legacy arcade emulation clusters', 'Looking for high color-gamut displays for designing custom avatar skins', 'Requires maximum cooling for long sector raids'"
)

st.markdown("---")


if st.button("⚡ SPAWN HIGH-IMMERSION RIGS (GENERATE) ⚡"):
    
    prompt = f"""
    You are James Halliday's digital avatar, Anorak, guiding a Gunter to build the ultimate OASIS immersion hardware setup.
    Provide exactly 3 real-world laptop hardware rigs widely available in the Indian retail market matching these metrics:
    - Max Budget: ₹{max_price:,} INR
    - Profile: {usage_type}
    - OS Setup: {os_choice}
    - Base Memory Target: {ram_target}
    - Custom Parameters: {custom_prompt if custom_prompt.strip() else 'None'}
    
    OUTPUT STRUCTURE DIRECTIVES:
    1. Do NOT write any introductory or concluding conversational filler text. Begin your output immediately with the first laptop details.
    2. Use the exact text tag `[SLOT_BREAK]` to separate your analysis for each laptop core.
    3. CRITICAL: Do NOT use markdown styles like headers (###), text links ([]()), or markdown images (![]()). You must construct the output for each machine using pure, clean HTML elements so it parses correctly inside web divisions.
    
    For each of the 3 laptops, structure your response text exactly like this HTML blueprint:
    <h3>Laptop Model Name</h3>
    <img src="Clean Public Image URL Source" alt="Laptop Image">
    <a href="https://www.google.com/search?q=INSERT_LAPTOP_CHASSIS_NAME_HERE+india&tbm=isch" target="_blank" rel="noopener noreferrer">🔎 Localized Retail Target</a>
    <br>
    <strong>OASIS Rig Hardware Specifications:</strong>
    <ul>
        <li><strong>Value Estimation:</strong> ₹[Price in INR]</li>
        <li><strong>Rig Configurations:</strong> [Details]</li>
        <li><strong>Inventory Upgrades:</strong> [Alternative upgrades available in India]</li>
        <li><strong>Gunter Quest Verdict:</strong> [Why this fits their OASIS quest profile]</li>
    </ul>
    """
    
    reels_placeholder = st.empty()
    
    
    with reels_placeholder.container():
        glitch_cols = st.columns(3)
        arcade_glyphs = ["🕹️", "👾", "🔑", "🥚", "INSERT COIN", "READY PLAYER ONE", "PARZIVAL", "ART3MIS", "ANORAK", "IOI-618"]
        for i in range(3):
            random_stream = f"{random.choice(arcade_glyphs)}\n{random.choice(arcade_glyphs)}\n{random.choice(arcade_glyphs)}"
            with glitch_cols[i]:
                st.markdown(f"""
                    <div class="slot-casing">
                        <div class="reel-header">LEVEL {i+1} LOADING</div>
                        <div class="spinning-content">
                            <h2 style="color:#ff007f !important; font-size: 28px; white-space: pre-line; text-align:center;">{random_stream}</h2>
                            <h4 style="color:#00ffff !important; text-align:center;">[ RENDERING_ASSETS ]</h4>
                            <h2 style="color:#ff007f !important; font-size: 28px; white-space: pre-line; text-align:center;">{random_stream[::-1]}</h2>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
    
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )
        
        
        safe_output = nh3.clean(
            response.text,
            tags={"h3", "img", "a", "br", "strong", "ul", "li", "p"},
            attributes={
                "a": {"href", "target", "rel"},
                "img": {"src", "alt"}
            },
            link_rel=None
        )
        
        laptop_slots = [block.strip() for block in safe_output.split("[SLOT_BREAK]") if block.strip()]
        
        time.sleep(1.0)
        
        reels_placeholder.empty()
        st.toast("🏆 EASTER EGG FOUND. OASIS RIG ARCHITECTURES MOUNTED.")
        st.success("🕹️ RIG ACQUISITION SUCCESSFUL. YOUR HIGH-IMMERSION HARDWARE LOOT:")
        
        final_reels = st.columns(3)
        for idx in range(min(len(laptop_slots), 3)):
            with final_reels[idx]:
                st.markdown(
                    f'<div class="slot-casing"><div class="reel-header">🏆 INVENTORY SLOT {idx+1}</div>{laptop_slots[idx]}</div>', 
                    unsafe_allow_html=True
                )
                
    except Exception as e:
        reels_placeholder.empty()
        st.error(f"❌ IOI INTERCEPT: Sixers fractured the inventory stream sequence: {e}")
