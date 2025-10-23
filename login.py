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
        # Direct JS redirect in the same tab
        redirect_target = "https://openneurolensdemo.streamlit.app"
        js_redirect = f"""
        <script type="text/javascript">
            window.location.replace("{redirect_target}");
        </script>
        """
        st.markdown(js_redirect, unsafe_allow_html=True)

        # Fallback clickable link
        st.write("If you are not redirected automatically, click here:")
        st.markdown(f"[Open main app]({redirect_target})")
    else:
        st.error("❌ Invalid username or password. Please try again.")
        st.info("Correct demo credentials are: `test` / `pw`")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.write(
    "Demo login. This is not a secure production authentication method. "
    "For production use, integrate proper authentication (OAuth, SSO, secure session tokens)."
)
