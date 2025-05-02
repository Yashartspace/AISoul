import streamlit as st
import pandas as pd

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

# ---------- GOOGLE SHEET LINKS ----------
pencil_sheet = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQv1HdtKDYMyYGVlQGnoX08LzYhzn-WYzHXKqRRKJXnNKUM8K7yTDmnKEct04tn3v-gDGGEqg1JpS3C/pub?output=csv"
color_sheet = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT8TPi-64c5U-h_OtGih-Z3FK9nLPx-YG7_7HnlJ3ah77N9LMP7zshs78rc1zS-q1j2R21VnUjKgDqa/pub?output=csv"

# ---------- LOAD DATA ----------
@st.cache_data
def load_data(sheet_url):
    return pd.read_csv(sheet_url)

pencil_data = load_data(pencil_sheet)
color_data = load_data(color_sheet)

# ---------- TABS FOR LEVELS ----------
tab1, tab2 = st.tabs(["✏ Pencil Sketching Levels", "🎨 Color Painting Levels"])

with tab1:
    st.header("Pencil Sketching 365 Level Plan")
    st.dataframe(pencil_data, use_container_width=True)

with tab2:
    st.header("Color Painting 365 Level Plan")
    st.dataframe(color_data, use_container_width=True)

st.markdown("---")

# ---------- DAILY PROMPT ----------
import random

prompts = [
    "Draw a memory you never want to forget.",
    "Sketch a feeling you can't describe with words.",
    "Imagine your dream world and draw it.",
    "Create a portrait of yourself 10 years in the future.",
    "Illustrate your favorite season as an abstract painting."
]

st.header("✨ Daily Prompt")
random.seed(pd.Timestamp.today().day)  # Changes daily
prompt = random.choice(prompts)
st.success(f"**Today's Prompt:** {prompt}")

st.markdown("---")

# ---------- ARTWORK UPLOAD ----------
st.header("📤 Upload Your Artwork")
uploaded_file = st.file_uploader("Upload an image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Your Uploaded Artwork", use_column_width=True)
    st.success("✅ Artwork uploaded successfully!")

st.markdown("---")

# ---------- ABOUT ----------
st.header("About")
st.write("Created by **Yaswanth Dasari**, World Record Holding Artist, Art Coach, Founder of Inspire & Create LLC.")
st.write("📧 Email: yaswanth.dasari@slu.edu | 🌐 Website: inspireandcreate.art | 📷 Instagram: @artist_yaswanth")

st.info('"Art speaks where words are unable to explain."')

