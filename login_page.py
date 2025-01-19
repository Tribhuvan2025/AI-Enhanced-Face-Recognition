import streamlit as st
from db_manager import validate_user

def login_page():
    # Center the login form using Streamlit form layout
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url('https://www.shutterstock.com/image-photo/child-boy-using-tablet-looking-600nw-2225757071.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(255, 255, 255, 0.5);
        background-blend-mode: overlay;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    col1,col2,col3=st.columns([3,8,3])
    with col2.form(key="login_form"):
        # Title
        st.title("Sign In") 

        # Email and Password inputs
        email = st.text_input("Email")
        image=st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
        
        # Submit button inside the form
        login_button = st.form_submit_button("Login",type="primary")

        # Handling form submission
        if login_button:
            user,message = validate_user(email, image)
            if user:
                st.success(message)
                # Set session state for successful login
                st.session_state["page"] = "user_home"
                st.session_state["user_email"] = email
                st.session_state["user_tab"] = "Loan Page"
                st.session_state["logged_in"] = True
                st.experimental_rerun()

            else:
                st.error("Invalid Email or Password!")
