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
st.set_page_config(layout="wide", initial_sidebar_state="auto")

# st.text("Research is hard enough as it is.\nFinding the right TEM provider shouldn't be.")

tab1, tab2, tab3, tab4 = st.tabs(["TEM Finder", "Guide", "About", "Contact"])

with tab1:
    # Display the table
    st.title('Transmission Eelectron Microscopy (TEM) Finder')
    st.markdown("## Find the right TEM provider for your needs")

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
        "Select the type of institution you want to work with",
        df["Type of institution"].unique(),
        default=df["Type of institution"].unique()
    )

    # Multi-select filter for type of organization
    selected_organization_types = st.sidebar.multiselect(
        "Select your organization type",
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
        col7, col8, col9 = st.columns(3)
        row1 = st.container()
        row2 = st.container()
        row3 = st.container()
        with row1:
            with col1:
                # st.subheader("Institution")
                st.markdown(f"### [{row['Name']}]({row['Website']})")
                st.text(f"Type: {row['Type of institution']}")
                if pd.notna(row["City"]) and pd.notna(row["State"]):
                    st.text(f"Location: {row['City']}, {row['State']}")

            with col2:
                st.subheader("Serving")
                markdown_for_service('Research')
                markdown_for_service('Clinical')

            
            with col3:
                st.subheader("Services")
                markdown_for_service('TEM')
                markdown_for_service('SEM')
                markdown_for_service('Cryo-EM')
                markdown_for_service('Sample prep')

        with row2:
            with col4:
                st.write("#")
                st.subheader("Pricing per sample")
                if pd.notna(row['Pricing per sample']):
                    st.text(f"$ {round(row['Pricing per sample'])}")
                else:
                    st.text("Coming soon...")

            with col5:
                st.write("#")
                if pd.notna(row['Pricing Caveats']):
                    st.subheader("Pricing caveats")
                    st.markdown(f"{row['Pricing Caveats']}")
            
            with col6:
                st.write("#")

                st.subheader("Turnaround")
                if pd.notna(row['Estimated turnaround (weeks)']):
                    st.text(f"{row['Estimated turnaround (weeks)']} weeks")
                else:
                    st.text("Coming soon...")

        with row3:
            with col7:
                st.write("#")
                st.subheader("Contact Info")
                st.markdown(f"Phone: {row['Phone']}")
                st.markdown(f"Email: {row['Email']}")
                if pd.notna(row['Contact Form']):
                    st.markdown(f"Contact Form: {row['Contact Form']}")
                st.write("#")
            
            with col8:
                st.write("#")
                st.subheader("Best way to contact")
                st.markdown(row['How to get a quote'])
            

        with st.expander("More services info"):
            st.markdown(f"{row['Detailed Services']}")

        if pd.notna(row['Additional Pricing information']):
            with st.expander("More pricing info"):
                st.markdown(f"{row['Additional Pricing information']}")

        if pd.notna(row['Additional turnaround info']):
            with st.expander("More turnaround info"):
                st.markdown(f"{row['Additional turnaround info']}")

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

    st.markdown("If you have any issues [please reach out](https://forms.gle/QM9wnpNZALQjGFVK9), we're here to help!")

with tab3:
    st.title("Research is hard enough as it is")
    st.text("Finding the right TEM provider shouldn't be.")
    st.write('---')

    st.markdown("**Biological esearchers are incredibly important**, however, it seems that in some areas the offerings provided simply aren't at the level we think they should be. This is the first step in our journey to help change that.")

    st.markdown("TEM specifically seems to be in a tough position. You either have expensive private companies that can provide quicker turnaround, or you have universities that can provide cheaper services but with longer and usually inconsistent turnaround times. Our goal is to build a TEM company that provides researchers with university prices and private company turnaround times (ideally faster).")

    st.markdown("If that seems interesting to you, we'd love to hear from you. The first step in this journey is validating our assumption that this is a real need, so if you could [take a quick minute to fill out this form](https://forms.gle/gt4Qgvip5xjMihFD8), we'd really appreciate it.")

    st.markdown("Either way, we hope you find this tool useful. [Let us know if we missed one](https://forms.gle/C5pqh7jE6mosbY1A8) and we'll add it!")



with tab4:
    st.title("Let's make TEM better together!")
    st.markdown("[Tell us what your current situation is and how it could be better](https://forms.gle/gt4Qgvip5xjMihFD8)")

    st.title("Let us know if we missed one")
    st.markdown("[Submit the missing provider here](https://forms.gle/C5pqh7jE6mosbY1A8)")

    st.title("TEM Finder isn't working right :(")
    st.markdown("[Tell us what's wrong](https://forms.gle/QM9wnpNZALQjGFVK9)")