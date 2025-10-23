# login.py
import streamlit as st

st.set_page_config(page_title="Login - OpenNeuroLens", layout="centered")

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
login = st.button("Login")

# Correct credentials
CORRECT_USER = "test"
CORRECT_PW = "pw"

# -------------------------------
# Login check
# -------------------------------
if login:
    st.session_state.login_attempts += 1

    if username == CORRECT_USER and password == CORRECT_PW:
        st.success("Login successful! Redirecting to main app...")

        # Full external URL of the main app
        redirect_target = "https://openneurolensdemo.streamlit.app"

        # JS redirect
        js = f"""
        <script>
            window.location.href = "{redirect_target}";
        </script>
        """
        st.markdown(js, unsafe_allow_html=True)

        # Fallback clickable link
        st.markdown(f"If you are not redirected automatically, click here: [Open main app]({redirect_target})")
    else:
        st.error("❌ Invalid username or password. Please try again.")
        st.info("Correct demo credentials are: `test` / `pw`")

# -------------------------------
