import streamlit as st

def show_socials_page():
    # Title of the App

    gradient_text_html = """
    <style>
    @keyframes gradient {
        0% { color: #ff0000; }
        25% { color: #00ff00; }
        50% { color: #0000ff; }
        75% { color: #ff00ff; }
        100% { color: #ff0000; }
    }

    .gradient-text {
        font-size: 3em;
        font-weight: bold;
        animation: gradient 5s infinite;
        display: inline;
    }    
    </style>
    <div class="gradient-text">DevPay</div><b style="color:blue">pro</b>
    """

    st.markdown(gradient_text_html, unsafe_allow_html=True)

    grad_subheading11 = """
    <style>
    .gradient-textt {
        font-weight: bold;
        background: -webkit-linear-gradient(left, red, orange);
        background: linear-gradient(to right, red, orange);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: 2em;
    }
    </style>
    <div class="gradient-textt">Acknowledgment</div>
    """

    st.markdown(grad_subheading11, unsafe_allow_html=True)

    # Acknowledgment Section
    st.markdown("""
    We would like to extend our heartfelt gratitude to our **Project Guide** and **Head of the Department of Computer Science and Engineering, Bangalore Institute of Technology** , **Dr. J Girija** Mam for her invaluable guidance and support throughout this project. Her insights and encouragement have been instrumental in the successful development of DevPay Pro.
    """)

    # Social Profiles Section
    grad_subheading121 = """
    <style>
    .gradient-textt {
        font-weight: bold;
        background: -webkit-linear-gradient(left, red, orange);
        background: linear-gradient(to right, red, orange);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: 2em;
    }
    </style>
    <div class="gradient-textt">Connect with Us</div>
    """

    st.markdown(grad_subheading121, unsafe_allow_html=True)


    
    # Create buttons for GitHub and LinkedIn profiles
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button('Github'):
            st.markdown("[GitHub Profile](https://github.com/aumjadhav8)")
            
    with col2:
        if st.button('LinkedIn'):
            st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/aumjadhav8)")

if __name__ == "__main__":
    show_socials_page()
