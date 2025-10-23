# login.py
import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Login - OpenNeuroLens", layout="centered")

# Simple header
st.title("OpenNeuroLens — Login")
st.markdown("Please enter your credentials to continue to the main app.")

# Keep minimal session state
if "login_attempts" not in st.session_state:
    st.session_state.login_attempts = 0

username = st.text_input("Username")
password = st.text_input("Password", type="password")
login = st.button("Login")

# Correct credentials
CORRECT_USER = "test"
CORRECT_PW = "pw"

if login:
    st.session_state.login_attempts += 1

    if username == CORRECT_USER and password == CORRECT_PW:
        st.success("Login successful! Redirecting to main app...")

        # Set query param so multipage Streamlit will open the app_web page (common pattern)
        # and inject JS to redirect the browser to the page param.
        # The JS fallback avoids relying on st.experimental_rerun which can be unstable in some hosts.
        redirect_target = "/?page=app_web.py"

        # Some deployments include a base path. If your app is served under a subpath, update redirect_target.
        js = f"""
        <script>
            // Try to redirect to the multipage page parameter that selects app_web
            window.location.href = "{redirect_target}";
        </script>
        """
        st.markdown(js, unsafe_allow_html=True)

        # Also provide a clickable fallback link for environments where JS is disabled
        st.markdown(f"If you are not redirected automatically, click here: [Open main app]({redirect_target})")

    else:
        st.error("❌ Invalid username or password. Please try again.")
        st.info("Correct demo credentials are: `test` / `pw`")

# Optional: small privacy notice / instructions
st.markdown("---")
st.write("Demo login. This is not a secure production authentication method. For production use, integrate proper authentication (OAuth, single-sign-on, secure session tokens).")
