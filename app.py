import streamlit as st
from google import genai
import nh3
import time
import random
import json
import urllib.parse  

st.set_page_config(page_title="Welcome To The Computer Matrix", page_icon="📟", layout="wide")

st.markdown("""
    <style>
    /* Monochrome Green Phosphor / Matrix Core Background */
    .stApp {
        background-color: #000000;
        color: #00ff00; 
        font-family: 'Courier New', Courier, monospace;
        background-image: linear-gradient(0deg, rgba(0, 30, 0, 0.5) 50%, rgba(0, 0, 0, 1) 50%);
        background-size: 100% 4px;
    }
    
    body { text-shadow: 0 0 4px #00ff00; }
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
        min-height: 560px;
        text-align: left;
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
        text-align: center;
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
    }

    .slot-casing img {
        border: 2px solid #00cc00;
        border-radius: 2px;
        box-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
        margin: 15px auto;
        display: block;
        max-width: 100%;
        height: auto;
    }
    
    .slot-casing a {
        color: #00ff00 !important;
        text-decoration: underline !important;
        text-shadow: 0 0 6px #00ff00;
        font-weight: bold;
        display: block;
        text-align: center;
        margin: 10px 0px;
    }
    </style>
""", unsafe_allow_html=True)


api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("🔑 ACCESS DENIED: INITIALIZE SAFE ENVIRONMENT SECRETS MATRIX.")
    st.stop()

client = genai.Client(api_key=api_key)

st.title("📟 THE MATRIX:LAPTOP DECRYPTER")
st.write("SYS_STATUS: [ OPERATIONAL ] // ENVIRONMENT: [ HARDENED_KERNEL ]")
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
    placeholder="e.g., 'Targeting localized compilation clusters...'"
)

st.markdown("---")

if st.button("⚡ EXTRICATE RAW CONSTRUCT (DECRYPT) ⚡"):
    
    
    prompt = f"""
    You are the Lead Systems Architect of the Zion mainframe network decoding encrypted hardware specifications.
    Return exactly 3 real-world laptop chassis models widely available in the Indian retail market matching these metrics:
    - Max Budget: ₹{max_price:,} INR
    - Profile: {usage_type}
    - OS Setup: {os_choice}
    - Base Memory Target: {ram_target}
    - Custom Parameters: {custom_prompt if custom_prompt.strip() else 'None'}
    
    CRITICAL STRUCTURE DIRECTIVE:
    You must return a valid, unquoted, raw JSON array containing exactly 3 objects. Do not wrap the JSON in markdown formatting text blocks like ```json.
    Each object in the array must contain these exact keys:
    {{
        "chassis_name": "Exact Name of the laptop model",
        "image_url": "Clean public image URL source link",
        "price_estimate": "Estimated price using the ₹ symbol",
        "core_specs": "Processor details, base ram values, hard drive capacities",
        "upgrades": "Specific components scalable or upgradeable in India",
        "verdict": "Clear architectural explanation of why this configuration answers the user parameters"
    }}
    """
    
    reels_placeholder = st.empty()
    
    
    with reels_placeholder.container():
        glitch_cols = st.columns(3)
        matrix_glyphs = ["1010", "ｦｱｳ", "ｼｵﾒ", "0110", "🔋📟", "🖳⚙️"]
        for i in range(3):
            random_stream = f"{random.choice(matrix_glyphs)}\n{random.choice(matrix_glyphs)}\n{random.choice(matrix_glyphs)}"
            with glitch_cols[i]:
                st.markdown(f"""
                    <div class="slot-casing">
                        <div class="reel-header">STREAM {i+1} RUNNING</div>
                        <div class="spinning-content">
                            <h2 style="color:#00ff00 !important; font-size: 32px; white-space: pre-line; text-align:center;">{random_stream}</h2>
                            <h4 style="color:#80ff80 !important; text-align:center;">[ SECURING_KERNEL ]</h4>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
    
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )
        
        
        raw_text = response.text.strip()
        
        if raw_text.startswith("```json"):
            raw_text = raw_text[7:-3].strip()
        elif raw_text.startswith("```"):
            raw_text = raw_text[3:-3].strip()
            
        laptop_data_list = json.loads(raw_text)
        
        time.sleep(1.0)
        reels_placeholder.empty()
        st.toast("🔓 DECRYPTION DATA CONSTRUCT VERIFIED SAFE.")
        st.success("📟 SIGNAL SECURED. DECRYPTED CONSTRUCT OBJECTS MOUNTED:")
        
        final_reels = st.columns(3)
        
        
        for idx, laptop in enumerate(laptop_data_list[:3]):
            
            clean_name = nh3.clean(str(laptop.get("chassis_name", "Unknown Chassis")))
            clean_price = nh3.clean(str(laptop.get("price_estimate", "TBD")))
            clean_specs = nh3.clean(str(laptop.get("core_specs", "")))
            clean_upgrades = nh3.clean(str(laptop.get("upgrades", "")))
            clean_verdict = nh3.clean(str(laptop.get("verdict", "")))
            
            
            search_query = urllib.parse.quote(f"{clean_name} laptop price india")
            secure_retail_url = f"[https://www.google.com/search?q=](https://www.google.com/search?q=){search_query}&tbm=isch"
            
    
            raw_img_url = laptop.get("image_url", "")
            clean_img_url = nh3.clean(raw_img_url) if (raw_img_url.startswith("http://") or raw_img_url.startswith("https://")) else ""

            html_payload = f"""
            <div class="slot-casing">
                <div class="reel-header">📟 CORE {idx+1} LOCKED</div>
                <h3>{clean_name}</h3>
                {"<img src='" + clean_img_url + "' alt='Chassis Frame'>" if clean_img_url else ""}
                <a href="{secure_retail_url}" target="_blank" rel="noopener noreferrer">🔎 Localized Retail Target</a>
                <br>
                <strong>Hardware Base Configuration Matrix:</strong>
                <ul>
                  <li><strong>Value Estimation:</strong> {clean_price}</li>
                  <li><strong>Core Configurations:</strong> {clean_specs}</li>
                  <li><strong>Expansion Upgrades:</strong> {clean_upgrades}</li>
                  <li><strong>Analytical Verdict:</strong> {clean_verdict}</li>
                </ul>
            </div>
            """
            with final_reels[idx]:
                st.markdown(html_payload, unsafe_allow_html=True)
                
    except Exception as e:
        reels_placeholder.empty()
        st.error(f"⚠️ INTEGRITY_ERROR: Data package failed validation firewalls: {e}")