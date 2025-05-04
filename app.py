import streamlit as st
import pandas as pd
import random

# ---------- PAGE CONFIGURATION ----------
st.set_page_config(
    page_title="ArtSoul AI – Healing Through Creativity",
    layout="wide"
)

# ---------- PAGE STYLING ----------
st.markdown(
    """
    <style>
    .main {background-color: #f4f4f9;}
    .stTabs [role="tab"] {
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
    }
    .stTabs [role="tab"][aria-selected="true"] {
        background-color: #a6c1ee;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- TITLE ----------
st.title("🎨 ArtSoul AI – Healing Through Creativity")
st.write("Created by **Yaswanth Dasari**, World Record Holding Artist, Art Coach, Founder of Inspire & Create LLC.")
st.write("📧 Email: yaswanth.dasari@slu.edu | 🌐 Website: inspireandcreate.art | 📷 Instagram: @artist_yaswanth")

st.markdown("---")

# ---------- GOOGLE SHEET CSV LINKS ----------
pencil_sheet = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQN6yCv0hKlmEoMH5oLVukyIkip0QvZkx27CqGmvUY7PWz3wwD5xFXOWpIGV6UtIAjqXBBy9eUg_e8B/pub?output=csv"
color_sheet = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQcOMrWVR3Yo9VGpblnoqEjVpVtKXIL8Lotxp9OacnMvAQ7qg8dROBiaDzZGZjyjQKBRtLTxj06zjpN/pub?output=csv"

# ---------- LOAD DATA ----------
@st.cache_data
def load_data(sheet_url):
    df = pd.read_csv(sheet_url)
    df.columns = df.columns.str.strip()
    return df

pencil_data = load_data(pencil_sheet)
color_data = load_data(color_sheet)

# ---------- TABS ----------
tab1, tab2 = st.tabs(["✏ Pencil Sketch Progress", "🎨 Color Painting Progress"])

# ---------- PENCIL SKETCH TAB ----------
with tab1:
    st.header("Your Pencil Sketching Progress")

    level = st.selectbox("Select Your Current Level (Pencil Sketching)", range(1, 366))
    st.success(f"Your Selected Level: {level} / 365")

    st.progress(level / 365)

    if 'Level' in pencil_data.columns:
        row = pencil_data[pencil_data['Level'] == level]
        if not row.empty:
            st.write(f"**Skill:** {row.iloc[0]['Skill']}")
            st.write(f"**Description:** {row.iloc[0]['Description']}")
            st.write(f"**AI Hint:** {row.iloc[0]['AI Hint']}")
        else:
            st.warning("Level data not found for this level.")
    else:
        st.error("❌ 'Level' column not found in Pencil Sketch sheet. Please check the header.")

# ---------- COLOR PAINTING TAB ----------
with tab2:
    st.header("Your Color Painting Progress")

    level2 = st.selectbox("Select Your Current Level (Color Painting)", range(1, 366))
    st.success(f"Your Selected Level: {level2} / 365")

    st.progress(level2 / 365)

    if 'Level' in color_data.columns:
        row2 = color_data[color_data['Level'] == level2]
        if not row2.empty:
            st.write(f"**Skill:** {row2.iloc[0]['Skill']}")
            st.write(f"**Description:** {row2.iloc[0]['Description']}")
            st.write(f"**AI Hint:** {row2.iloc[0]['AI Hint']}")
        else:
            st.warning("Level data not found for this level.")
    else:
        st.error("❌ 'Level' column not found in Color Painting sheet. Please check the header.")

st.markdown("---")

# ---------- DAILY PROMPT ----------
prompts = [
    "Draw a memory you never want to forget.",
    "Sketch a feeling you can't describe with words.",
    "Imagine your dream world and draw it.",
    "Create a portrait of yourself 10 years in the future.",
    "Illustrate your favorite season as an abstract painting."
]

st.header("✨ Daily Prompt")
random.seed(pd.Timestamp.today().day_of_year)
prompt = random.choice(prompts)
st.success(f"**Today's Prompt:** {prompt}")

st.markdown("---")

# ---------- ARTWORK UPLOAD & EVALUATION ----------
st.header("📤 Upload Your Artwork")
uploaded_file = st.file_uploader("Upload an image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Your Uploaded Artwork", use_column_width=True)
    st.success("✅ Artwork uploaded successfully!")

    # ---------- Mock Evaluation ----------
    st.subheader("🎯 AI Evaluation Result")
    score = random.randint(70, 95)
    st.info(f"Your artwork received a score of **{score}%**")

    if score >= 80:
        st.success("✅ Excellent work! You may proceed to the next level.")
    else:
        st.warning("❗ Please practice this level again before proceeding.")

st.markdown("---")

# ---------- ARTSOUL AI CHATBOT ----------
st.header("🤖 ArtSoul AI Chatbot")

user_input = st.text_input("Ask ArtSoul AI anything about your art journey:")

if user_input:
    st.write("🧠 ArtSoul AI:", "I'm here to guide you! Currently, this is a demo chatbot. Soon, I'll provide real-time feedback and support!")

st.markdown("---")

# ---------- ABOUT ----------
st.header("About")
st.write("Created by **Yaswanth Dasari**, World Record Holding Artist, Art Coach, Founder of Inspire & Create LLC.")
st.write("📧 Email: yaswanth.dasari@slu.edu | 🌐 Website: inspireandcreate.art | 📷 Instagram: @artist_yaswanth")

st.info('"Art speaks where words are unable to explain."')
