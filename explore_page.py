import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

# Create a function to compile the countries with smaller values into "Others" categories
def compile_countries(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = "Others"
    return categorical_map

# Create a function to standardize and clean the coding experience column
# Convert Coding Experience Column into float data type
def clean_yearsCodePro(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

# Clean education column into a few categories
def clean_edLevel(x):
    if "Bachelor’s degree" in x:
        return "Bachelor's degree"
    if "Master’s degree" in x:
        return "Master's degree"
    if "Professional degree" in x or "Other doctoral" in x:
        return "Postgraduate"
    return "Less than a Bachelors"

@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    # Extracting Columns that are being used for model training
    df = df[["Country", "EdLevel", "YearsCodePro", "WorkExp", "Employment", "RemoteWork", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly":"Salary"}, axis = 1)
    df = df[df["Salary"].notnull()]
    df= df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df= df.drop("Employment", axis = 1)
    country_map = compile_countries(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)

    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "Others"]

    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_yearsCodePro)
    df['EdLevel'] = df["EdLevel"].apply(clean_edLevel)

    return df

df = load_data()

def show_explore_page():

    grad_subheading11 = """
    <style>
    .gradient-textt {
        font-weight: bold;
        background: -webkit-linear-gradient(left, red, orange);
        background: linear-gradient(to right, red, orange);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: 2.5em;
    }
    </style>
    <div class="gradient-textt">Explore Developers Salary Insights</div>
    """

    st.markdown(grad_subheading11, unsafe_allow_html=True)

    st.write(
        """##### Stack Overflow Developer Survey 2023"""
        )
    flow_chart_image = "devsurvey.png"
    st.image(flow_chart_image, use_column_width=True, caption='StackOverflow 2023')

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    # equal ensures that pie chart is drawn as a circle
    ax1.axis("equal")      

    st.write("""#### Number of Data from different countries""") 

    st.pyplot(fig1)

    st.write("""#### Mean Salary Based on Country""") 

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write("""#### Mean Salary Based on Experience""") 

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)

    # Add plot for model accuracy and median salary country-wise
    # Assuming you have calculated the accuracy scores and stored in `model_accuracies` and `median_salaries`
    
    st.write("""#### Model Accuracy""")
    
    model_accuracies = { # example data, replace with your actual data
        "Linear Regression": 0.53,
        "Decision Tree": 0.68,
        "Random Forest": 0.75
    }
    
    accuracies_df = pd.DataFrame(list(model_accuracies.items()), columns=['Model', 'R2 Score'])
    st.bar_chart(accuracies_df.set_index('Model'))

    st.write("""#### Median Salary Based on Country""")

    median_salaries = df.groupby("Country")["Salary"].median().sort_values(ascending=True)
    st.bar_chart(median_salaries)

# Call the function to display the explore page
if __name__ == "__main__":
    show_explore_page()
