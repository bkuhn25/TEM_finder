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

    with col2:
        st.header("Type")
        st.text(row['Type of institution'])

      
    with col3:
        st.header("Serving")
        # write markdown for the research category where if it is yes it shows a check emoji and if it is no it shows a cross emoji
        st.markdown(markdown_for_service('Research'))
        st.markdown(markdown_for_service('Clinical'))

        # refactor the markdown above to be a function that takes in a string and returns the markdown
        


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
