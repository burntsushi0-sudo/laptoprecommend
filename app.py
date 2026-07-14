import streamlit as st
from google import genai
st.set_page_config(page_title="Cybercore Laptop Matchmaker", page_icon="⚡", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #0f1116; color: #ffffff; }
    .stButton>button { 
        background-color: #6200ea; color: white; border-radius: 8px; 
        font-weight: bold; width: 100%; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #3700b3; color: #00ffcc; }
    </style>
""", unsafe_allow_html=True)

# Securely pull API Key
api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("🔑 Missing API Key! Configure GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()

client = genai.Client(api_key=api_key)

# 2. Header Section
st.title("⚡ Cybercore Laptop Matchmaker")
st.caption("Stop reading confusing spec sheets. Let AI find your perfect digital companion.")
st.markdown("---")

# 3. Sidebar: Gamified Setup Panel
st.sidebar.header("🛠️ Configure Your Vibe")

# Creative Budget Slider instead of a text box
budget_usd = st.sidebar.slider("What's the financial damage? (Budget in USD)", 300, 3500, 1200, step=100)

# Creative Persona archetypes
user_persona = st.sidebar.selectbox(
    "Which best describes you?",
    [
        "☕ Coffee Shop Hustler (Needs massive battery & lightweight frame)",
        "🎮 Frame-Rate Fiend (Needs raw GPU power, RGB, and heavy cooling)",
        "🎓 Broke Student (Maximum value, needs to survive 4 years of abuse)",
        "🎬 Pixel Perfectionist (4K video editing, color-accurate screen vital)",
        "🚀 Code Wizard (Needs 32GB+ RAM, compilation speed, comfy keyboard)"
    ]
)

# Interactive Screen Size Toggle
screen_vibe = st.sidebar.radio(
    "Screen Preferences",
    ["Ultra-portable (13-14\")", "The Sweet Spot (15-16\")", "Desktop Replacement (17\"+)" ]
)

# 4. Main Page: Choosing the AI's Personality
st.subheader("🤖 Step 2: Choose Your AI Advisor")
ai_personality = st.radio(
    "Select your advisor's tone:",
    [
        "🔥 Brutally Honest Tech Reviewer (Will roast bad components and give you the raw truth)",
        "🧘 Gentle Budget Guru (Focuses heavily on saving you money and finding hidden gems)",
        "✨ Futuristic Cyberpunk Guide (Immersive sci-fi flavor, treats hardware like cybernetic upgrades)"
    ],
    horizontal=True
)

extra_quirks = st.text_input("Any specific dealbreakers? (e.g., 'Must have an SD card slot', 'No loud fans')", placeholder="Type here...")

# 5. The Trigger & Creative Generation Logic
if st.button("✨ Summon My Recommendations"):
    
    # Custom instructions fed to Gemini based on the selected personality
    personality_prompt = ""
    if "Brutally Honest" in ai_personality:
        personality_prompt = "Act as a brutally honest, highly critical, witty tech reviewer. Roast choices that don't make sense for the budget, call out bad manufacturer habits, and give zero-fluff reality checks."
    elif "Gentle Budget" in ai_personality:
        personality_prompt = "Act as a warm, encouraging, financially conscious hardware coach. Emphasize saving money, avoiding over-speccing, and highlighting the best price-to-performance value."
    else:
        personality_prompt = "Act as a rogue Netrunner from a cyberpunk universe. Treat the laptop search like buying black-market cyberware decks, using futuristic slang, and analyzing technical stats as combat specs."

    # Stitch everything together into a creative prompt
    prompt = f"""
    {personality_prompt}
    
    Match a laptop setup for a user with these constraints:
    - Target Budget: ${budget_usd} USD
    - User Profile: {user_persona}
    - Form Factor Size: {screen_vibe}
    - Specific Dealbreakers/Wants: {extra_quirks if extra_quirks else "None"}
    
    Provide 3 distinct real-world laptop models currently on the market.
    For each machine, break down the exact CPU/RAM/Storage specs, evaluate the battery/screen based on their profile, and give your definitive verdict in your assigned persona character voice.
    """
    
    with st.spinner("🧠 Syncing neural pathways to the tech market..."):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            
            # Celebratory visual burst on screen!
            st.balloons()
            
            st.success("🤖 Matrix Sync Complete! Here are your matches:")
            st.markdown(response.text)
            
        except Exception as e:
            st.error(f"An error occurred while linking to the network: {e}")