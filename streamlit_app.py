import streamlit as st
import pandas as pd

def markdown_for_service(service: str):
    title_col, value_col = st.columns(2)
    with title_col:
        st.markdown(f"**{service.title()}:**")
    with value_col:
        st.markdown(':white_check_mark:' if row[service] == 'yes' else ':x:')

# Load the CSV data
csv_path = 'TEM_providers.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_path)

# Set the page config as wide
st.set_page_config(layout="wide")

# st.text("Research is hard enough as it is.\nFinding the right TEM provider shouldn't be.")

tab1, tab2, tab3, tab4 = st.tabs(["TEM Finder", "Guide", "About", "Contact"])

with tab1:
    # Display the table
    st.title('TEM Finder')

    # Filtering options
    st.sidebar.title('Filter Options')

    # Multi-select filter for services
    selected_services = st.sidebar.multiselect(
        "Select services you need",
        ["TEM", "SEM", "Cryo-EM", "Sample prep"],
        default=["TEM"]
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
        default=["Research"]
    )

    # Filter DataFrame based on selected services and institution types
    filtered_df = df[
        (df[selected_services].apply(lambda row: all(val == "yes" for val in row), axis=1)) &
        (df["Type of institution"].isin(selected_institution_types)) &
        (df[selected_organization_types].apply(lambda row: all(val == "yes" for val in row), axis=1))
    ]

    st.text(f"Showing {len(filtered_df)} of {len(df)} providers")
    st.write('---')

    for index, row in filtered_df.iterrows():
        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)
        row1 = st.container()
        row2 = st.container()
        with row1:
            with col1:
                st.subheader("Name")
                st.markdown(f"[{row['Name']}]({row['Website']})")

            with col2:
                st.subheader("Type")
                st.text(row['Type of institution'])

            
            with col3:
                st.subheader("Serving")
                # write markdown for the research category where if it is yes it shows a check emoji and if it is no it shows a cross emoji
                markdown_for_service('Research')
                markdown_for_service('Clinical')

        with row2:
            with col4:
                st.subheader("Services")
                markdown_for_service('TEM')
                markdown_for_service('SEM')
                markdown_for_service('Cryo-EM')
                markdown_for_service('Sample prep')

            with col5:
                st.subheader("Contact Info")
                st.markdown(f"Phone: {row['Phone']}")
                st.markdown(f"Email: {row['Email']}")
                if pd.notna(row['Contact Form']):
                    st.markdown(f"Contact Form: {row['Contact Form']}")

            
            with col6:
                st.subheader("Best way to contact")
                st.markdown(row['How to get a quote'])
            

        with st.expander("More services info"):
            st.markdown(f"{row['Detailed Services']}")

        if pd.notna(row['Additional Contact Info']):
            with st.expander("More contact info"):
                st.markdown(f"{row['Additional Contact Info']}")
            

        st.write('---')

with tab2:
    
    st.markdown("## Step 1:")
    st.markdown("From the filters on the left")
    st.markdown("- Select the services you need")
    st.markdown("- Select the type of institution(s) you want to work with")
    st.markdown("- Select your organization type")
    st.write('---')

    st.markdown("## Step 2:")
    st.markdown("- Select the provider(s) that best fits your needs from the list")
    st.markdown("- Reach out to get some TEM done baby and change the world!")
    st.write('---')

    st.markdown("If you want to reset the filters simply refresh the page and everything will reset.")
    st.write('---')

    st.markdown("If you have any issues please reach out, we're here to help!")

with tab3:
    st.title("Research is hard enough as it is")
    st.text("Finding the right TEM provider shouldn't be.")
    st.write('---')

    st.markdown("**Biological esearchers are incredibly important**, however, it seems that in some areas the offerings provided simply aren't at the level we think they should be. This is the first step in our journey to help change that.")

    st.markdown("TEM specifically seems to be in a tough position. You either have expensive private companies that can provide quicker turnaround, or you have universities that can provide cheaper services but with longer and usually inconsistent turnaround times. Our goal is to build a TEM company that provides researchers with university prices and private company turnaround times (ideally faster).")

    st.markdown("If that seems interesting to you, we'd love to hear from you. The first step in this journey is validating our assumption that this is a real need, so if you could take a few minutes to fill out the form below, we'd really appreciate it.")

    st.markdown("Either way, we hope you find this tool useful. Let us know if we missed one and we'll add it!")