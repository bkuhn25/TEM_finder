import streamlit as st
import pandas as pd

def markdown_for_service(service: str):
    return f"**{service.title()}:** {' :white_check_mark:' if row[service] == 'yes' else ':x:'}"

# Load the CSV data
csv_path = 'TEM_providers.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_path)

# Display the table
st.title('TEM Finder')

# Show the raw data as a table
st.write('## Raw Data')
st.dataframe(df)

# Filtering options
st.sidebar.title('Filter Options')

# Multi-select filter for services
selected_services = st.sidebar.multiselect(
    "Select services you need",
    ["TEM", "SEM", "Cryo-EM", "Sample prep"]
)

# Multi-select filter for type of institution
selected_institution_types = st.sidebar.multiselect(
    "Select type of institution",
    df["Type of institution"].unique(),
    default=df["Type of institution"].unique()
)

# Multi-select filter for type of organization
selected_organization_types = st.sidebar.multiselect(
    "Select organization types the provider serves",
    ["Clinical", "Research",],
    default=["Clinical", "Research"]
)

# Filter DataFrame based on selected services and institution types
filtered_df = df[
    (df[selected_services].apply(lambda row: all(val == "yes" for val in row), axis=1)) &
    (df["Type of institution"].isin(selected_institution_types)) &
    (df[selected_organization_types].apply(lambda row: all(val == "yes" for val in row), axis=1))
]

for index, row in filtered_df.iterrows():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Name")
        st.markdown(f"[{row['Name']}]({row['Website']})")

        st.header("Services")
        st.markdown(markdown_for_service('TEM'))
        st.markdown(markdown_for_service('SEM'))
        st.markdown(markdown_for_service('Cryo-EM'))
        st.markdown(markdown_for_service('Sample prep'))

    with col2:
        st.header("Type")
        st.text(row['Type of institution'])

        st.header("Contact Info")
        st.markdown(f"Phone: {row['Phone']}")
        st.markdown(f"Email: {row['Email']}")
        if pd.notna(row['Contact Form']):
            st.markdown(f"Contact Form: {row['Contact Form']}")

      
    with col3:
        st.header("Serving")
        # write markdown for the research category where if it is yes it shows a check emoji and if it is no it shows a cross emoji
        st.markdown(markdown_for_service('Research'))
        st.markdown(markdown_for_service('Clinical'))

        st.header("Best way to contact")
        st.markdown(row['How to get a quote'])
        

    with st.expander("More services info"):
        st.markdown(f"{row['Detailed Services']}")

    if pd.notna(row['Additional Contact Info']):
        with st.expander("More contact info"):
            st.markdown(f"{row['Additional Contact Info']}")
        

    st.write('---')

