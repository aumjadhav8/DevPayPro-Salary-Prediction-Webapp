import streamlit as st
import streamlit_option_menu
from streamlit_option_menu import option_menu
from predict_page import show_predict_page
from explore_page import show_explore_page
from home_page import show_home_page
from social_page import show_socials_page
logo_path = "menulogo.png"

with st.sidebar:
    st.image(logo_path, use_column_width=True)
    st.title("Main Menu")
    selected2 = option_menu(None, ["Home", "Predict", "Explore", 'Socials'], 
    icons=['house', 'cloud-upload', "search", 'gear'], 
    menu_icon="cast", default_index=1, orientation="vertical")


if selected2 == "Predict":
    show_predict_page()
elif selected2=="Explore":
    show_explore_page()
elif selected2=="Home":
    show_home_page()
elif selected2=="Socials":
    show_socials_page()
