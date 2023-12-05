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

for index, row in df.iterrows():
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

# # Filtering options
# st.sidebar.title('Filter Options')

# # Filtering options
# st.sidebar.title('Filter Options')

# # Add filtering widgets based on column types
# for column in df.columns:
#     filter_options = st.sidebar.multiselect(f'Select {column}:', df[column].unique())
#     if filter_options:
#         df = df[df[column].isin(filter_options)]

# # Display filtered data
# st.write('## Filtered Data')

# # Display filtered data with custom formatting
# for index, row in df.iterrows():
#     st.write('### Name:', row['Name'])
#     st.write('**Type of institution:**', row['Type of institution'])
#     st.write('**Services:**', row['Services'], unsafe_allow_html=True)
#     st.write('**Instruments:**', row['Instruments'])
#     st.write('**Website:**', row['Website'])
#     st.write('**Contact:**', row['Contact'], unsafe_allow_html=True)
#     st.write('**How to get a quote:**', row['How to get a quote'])
#     st.write('---')
