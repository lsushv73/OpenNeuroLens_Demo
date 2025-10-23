# login.py
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Login - OpenNeuroLens", layout="centered")

# -------------------------------
# Paths
# -------------------------------
BASE_DIR = Path(__file__).parent
EEGB_DIR = BASE_DIR / "static" / "EEGB"
BG_IMAGE = EEGB_DIR / "EEGB1.jpg"

# -------------------------------
# Background (works in Streamlit web)
# -------------------------------
if BG_IMAGE.exists():
    # Use relative path from the app
    bg_path = str(BG_IMAGE).replace("\\", "/")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{bg_path}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning(f"⚠️ Background image not found at: {BG_IMAGE}")

# -------------------------------
# Header
# -------------------------------
st.markdown("Welcome to:")
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
        st.success("✅ Login succeeded!")
        # Redirect (use multipage app navigation in Streamlit)
        st.markdown(
            """
            <script>
            window.location.href = '/?page=app_web';
            </script>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error("❌ Invalid username or password. Please try again.")
        st.info("Correct demo credentials are: `test` / `pw`")

# -------------------------------
# Footer / Demo notice
# -------------------------------
st.markdown("---")
st.write(
    "Demo login. This is not a secure production authentication method. "
    "For production use, integrate proper authentication (OAuth, SSO, secure session tokens)."
)
