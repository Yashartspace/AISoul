import streamlit as st
import random

# ------------------ Streamlit Page Setup ---------------------
st.set_page_config(page_title="ArtSoul AI – Healing Through Creativity", layout="wide")

# ------------------ Sidebar Navigation -----------------------
st.sidebar.markdown("<h2 style='color:white;'>Navigation</h2>", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Go to",
    ["🏠 Home", "💬 Art Chat AI", "📝 Daily Prompt", "📤 Upload Artwork", "📊 Contact / About"]
)

# ------------------ Footer -----------------------
def footer():
    st.markdown("---")
    st.markdown(
        "<center><i>Art speaks where words are unable to explain.</i><br>"
        "ArtSoul AI © 2025 | Created by Yaswanth Dasari | Inspire & Create LLC</center>",
        unsafe_allow_html=True
    )

# ------------------ Home Page -----------------------
def show_home():
    st.title("🎨 Welcome to ArtSoul AI – Healing Through Creativity")
    st.write("""
    Welcome to **ArtSoul AI**, your personal art therapy and creativity coach.
    
    **About Me:**  
    Created by **Yaswanth Dasari**  
    - World Record Holding Artist  
    - Art Coach  
    - Founder of Inspire & Create LLC

    **Our Mission:**  
    At Inspire & Create LLC, we are committed to helping people unlock their creativity and find healing through art. 
    Our mission is to make art learning and emotional growth accessible to everyone. 
    Art has the power to change lives, boost mental health, and inspire personal breakthroughs.
    
    **What You Can Do Here:**  
    - Get daily drawing prompts  
    - Chat with your AI art mentor  
    - Upload your artwork and track your progress  
    - Stay inspired and connected with a community of creators

    **Contact:**  
    Email: yaswanth.dasari@slu.edu  
    Website: inspireandcreate.art  
    Instagram: @artist_yaswanth
    """)

    st.success("Your current level: Beginner (Level 1)")

    footer()

# ------------------ Art Chat AI Page -----------------------
def show_chat():
    st.title("💬 Talk to Your Art Mentor AI")
    user_input = st.text_input("Ask a question or share a thought:")
    if st.button("Ask AI"):
        st.info("🤖 AI says:")
        st.write("Hello! I'm your creative guide. Let's overcome art blocks and unlock new ideas together!")
        st.warning("Note: Real AI chat will be added soon.")
    footer()

# ------------------ Daily Prompt Page -----------------------
def show_prompt():
    st.title("📝 Today's Drawing Prompt")
    prompts = [
        "Draw a memory you never want to forget.",
        "Sketch a feeling you can't describe with words.",
        "Imagine your dream world and draw it.",
        "Create a portrait of yourself 10 years in the future.",
        "Express the concept of hope using only lines and shapes."
    ]
    st.success(random.choice(prompts))
    footer()

# ------------------ Upload Artwork Page -----------------------
def show_upload():
    st.title("📤 Upload Your Artwork")
    uploaded = st.file_uploader("Choose an image (jpg, jpeg, png)", type=["png", "jpg", "jpeg"])
    if uploaded:
        st.image(uploaded, width=400)
        st.success("Artwork uploaded successfully! AI feedback coming soon.")
        st.success("Congratulations! You've advanced to Level 2 🎉")
    footer()

# ------------------ Contact/About Page -----------------------
def show_about():
    st.title("📊 About ArtSoul AI")
    st.write("""
    **ArtSoul AI** empowers artists and individuals through guided creativity, 
    AI mentorship, and positive emotional support.

    **Creator:** Yaswanth Dasari  
    Email: yaswanth.dasari@slu.edu  
    Website: inspireandcreate.art  
    Instagram: @artist_yaswanth
    """)
    footer()

# ------------------ Page Routing -----------------------
if page == "🏠 Home":
    show_home()
elif page == "💬 Art Chat AI":
    show_chat()
elif page == "📝 Daily Prompt":
    show_prompt()
elif page == "📤 Upload Artwork":
    show_upload()
elif page == "📊 Contact / About":
    show_about()

