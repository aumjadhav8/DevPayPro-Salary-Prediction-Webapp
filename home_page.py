import streamlit as st
import streamlit_shadcn_ui as ui

def show_home_page():
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
    ui.badges(badge_list=[("Machine Learning", "default"), ("Mini Project", "secondary"), ("StreamLit", "default"), ("Python", "destructive"), ("Developers", "destructive")], class_name="flex gap-2", key="badges1")


    st.markdown("""
    DevPay Pro is a groundbreaking solution tailored for the Indian software industry, crafted to meet the dynamic needs of developers seeking clarity on their earnings potential. Addressing the complexities of fluctuating market demands, diverse skill sets, and regional nuances, this platform provides unparalleled insights into software developer compensation trends across India. With its intuitive interface and robust backend architecture, DevPay Pro offers personalized salary forecasts, empowering developers with the knowledge they need to navigate their careers effectively in the ever-evolving landscape of the Indian tech sector. 
    """)
    grad_subheading11 = """
    <style>
    .gradient-textt {
        font-weight: bold;
        background: -webkit-linear-gradient(left, red, orange);
        background: linear-gradient(to right, red, orange);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: 3em;
    }
    </style>
    <div class="gradient-textt">About Data !</div>
    """

    st.markdown(grad_subheading11, unsafe_allow_html=True)

    cols = st.columns(4)
    with cols[0]:
        ui.metric_card(title="Number of Surveyers", content="89,184", description="Data is Collected from StackOverflow's 2023 Developers Survey.", key="card1")
    with cols[1]:
        ui.metric_card(title="Hours Taken", content="40+ hrs", description="The project consumed about 40+ hours of working, including all aspects.", key="card2")
    with cols[2]:
        ui.metric_card(title="Number of Regression Models", content="3", description="Linear Regression, Decision Tree, Random Forest", key="card3")
    with cols[3]:
        ui.metric_card(title="Features Considered", content="5/22", description="Country, Age, Degree, Coding Experience, Professional Coding Experience", key="card4")

    grad_subheading1 = """
    <style>
    .gradient-textt {
        font-weight: bold;
        background: -webkit-linear-gradient(left, red, orange);
        background: linear-gradient(to right, red, orange);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: 3em;
    }
    </style>
    <div class="gradient-textt">How Does it Work?</div>
    """

    st.markdown(grad_subheading1, unsafe_allow_html=True)
    st.markdown("""
    DevPay Pro heralds a transformative software solution tailored explicitly for the Indian software development community, meticulously crafted to tackle the unique challenges faced by developers in the region. This innovative platform offers unprecedented insights into software developer earnings across India, providing invaluable clarity amidst the dynamic landscape of the tech industry. With its intuitive interface and robust backend architecture, DevPay Pro empowers developers with personalized salary projections, enabling informed career decisions in an ever-evolving market. Much like its predecessor, DevPay Pro boasts scalability and affordability, simplifying the process of accessing crucial salary data while significantly reducing overhead costs associated with traditional methods. By equipping developers with the tools they need to navigate their professional trajectories effectively, DevPay Pro emerges as an indispensable asset for individual growth and industry advancement.
    """)

    st.write("""### Flow Chart for DevPay""")
    flow_chart_image = "null.png"
    st.image(flow_chart_image, use_column_width=True, caption='Flow Chart for DevPay')

    grad_subheading2 = """
    <style>
    .gradient-textt {
        font-weight: bold;
        background: -webkit-linear-gradient(left, red, orange);
        background: linear-gradient(to right, red, orange);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: 3em;
    }
    </style>
    <div class="gradient-textt">🌐 Flow of DevPay</div>
    """

    st.markdown(grad_subheading2, unsafe_allow_html=True)
    st.subheader("🛠️ Data Preparation")
    st.markdown("""
    - Download Dataset from `StackOverFlow`
    - Load `survey_results_public.csv` into Pandas DataFrame
    - Filter dataset for industry and country
    - Create columns for employment categories
    - Add columns for number of technologies
    - Select and filter relevant columns
    - Categorize and bin variables
    - Replace years experience outliers
    - Label encode categorical variables
    - Prepare data for training
    """)

    st.subheader("🤖 Model Training")
                
    st.markdown("""
    - Define regression models dictionary
    - Split data into training/testing sets
    - Standardize features
    - Train models on training set
    - Evaluate models on testing set
    - Print results table""")

    st.subheader("🔍 Feature Importance")
    st.markdown("""
    - Train Random Forest Regressor
    - Extract feature importances
    - Print sorted importances
    """)
    st.subheader("💾 Model Saving")
    st.markdown("""
    - Save best model and encoders with Pickle
    """)
    st.subheader("💰 Salary Prediction")
    st.markdown("""
    - Load model and encoders
    - Define input preparation function
    - Create Streamlit web app for predictions""")

    st.subheader("🚫 Error Handling")
    st.markdown("""
    - Handle exceptions in web app""")

    st.subheader("🚀 Deployment")
    st.markdown("""
    - Deploy web app on Streamlit
    """)


if __name__ == "__main__":
    show_home_page()
