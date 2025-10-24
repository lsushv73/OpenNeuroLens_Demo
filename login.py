# login.py
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Login - OpenNeuroLens", layout="centered")

# -------------------------------
# Paths
# -------------------------------
BASE_DIR = Path(__file__).parent
IMG_PATH = BASE_DIR / "static" / "EEGB" / "ONL.png"  # adjust path if needed

# -------------------------------
# Show image
# -------------------------------
# Create 3 columns: left, center, right
col1, col2, col3 = st.columns([1, 2, 1])

# Put the image in the center column
with col2:

    if IMG_PATH.exists():
        st.image(str(IMG_PATH), width=250)
        #st.image(str(IMG_PATH), use_container_width=True)
    else:
        st.error(f"⚠️ Image not found: {IMG_PATH}")

# -------------------------------
# Header
# -------------------------------
st.title("OpenNeuroLens")
st.markdown("Please enter your credentials to continue to the main app.")

# -------------------------------
# Session state
# -------------------------------
if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = 0

username = st.text_input("Username")
password = st.text_input("Password", type="password")
login_btn = st.button("Login")

# Correct credentials
CORRECT_USER = "test"
CORRECT_PW = "pw"

# -------------------------------
# Login check
# -------------------------------
if login_btn:
    st.session_state.login_attempts += 1

    if username == CORRECT_USER and password == CORRECT_PW:
        # Direct JS redirect in the same tab (optional)
        redirect_target = "https://openneurolens.streamlit.app"
        js_redirect = f"""
        <script type="text/javascript">
            window.location.replace("{redirect_target}");
        </script>
        """
        st.markdown(js_redirect, unsafe_allow_html=True)

        # Fallback clickable link
        st.write("✅ Login succeeded!")
        st.markdown(f"[Open main app]({redirect_target})")
    else:
        st.error("❌ Invalid username or password. Please try again.")
        st.info("Correct demo credentials are: `test` / `pw`")

# -------------------------------
# Footer / Demo notice
# -------------------------------

