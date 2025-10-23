import streamlit as st

st.set_page_config(page_title="Login - OpenNeuroLens", layout="centered")

st.markdown("Welcome to:")
st.title("OpenNeuroLens")
st.markdown("Please enter your credentials to continue to the main app.")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "show_app" not in st.session_state:
    st.session_state.show_app = False

username = st.text_input("Username")
password = st.text_input("Password", type="password")
login_btn = st.button("Login")

CORRECT_USER = "test"
CORRECT_PW = "pw"

if login_btn:
    if username == CORRECT_USER and password == CORRECT_PW:
        st.session_state.logged_in = True
        st.session_state.show_app = True
        st.success("✅ Login successful! You can now open the main app in the sidebar.")
    else:
        st.error("❌ Invalid username or password. Please try again.")

st.markdown("---")
st.write(
    "Demo login. For production, implement proper authentication (OAuth, SSO, secure session tokens)."
)
