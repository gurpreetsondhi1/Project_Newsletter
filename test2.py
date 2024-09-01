import streamlit as st
import pandas as pd

# Function to navigate between pages
def go_to_page(page_name):
    st.session_state.current_page = page_name

# Initialize session state for tracking the current page
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"  # Set the default page to Home

# Set page configuration
st.set_page_config(page_title='Axtria Newsletter', layout='wide')

# Load data from the Excel file
file_path = r'https://raw.githubusercontent.com/gurpreetsondhi1/Project_Newsletter/2228440e4eb86a2d53ffdbb9fccc6273154e7124/text.xlsx'  


try:
    # Read the Excel file into a DataFrame
    data = pd.read_excel(file_path, sheet_name=0)  # Specify the sheet if needed
    data1 = pd.read_excel(file_path, sheet_name='Sheet2')
    
    # Display content based on the current page
    
    if st.session_state.current_page == "Home":
        # Display the main title of the newsletter
        st.markdown(
            """
            <h1 style='text-align: center; font-size: 60px; color: black;'>The Axtria Times</h1>
            """, 
            unsafe_allow_html=True
        )
        #st.subheader('August | Issue 1')
        
        st.divider()
        
        # Iterate through each row of the data
        for index, row in data.iterrows():
            # Display content for each row
            if(index % 2==0):
                with st.container():
                    col1, col2 = st.columns([1, 2])

                # Display the image if the path is not empty
                if pd.notna(row['Image Path']):
                    col1.image(row['Image Path'], width=400)  # Adjust the width as needed
      
                # Display Header, Sub Header, and Text values
                if pd.notna(row['Header']):
                    col2.title(row['Header'])
                if pd.notna(row['Sub Header']):
                    col2.subheader(row['Sub Header'])
                if pd.notna(row['Text']):
                    col2.write(row['Text'])

                # Add a "Read More" button to navigate to the stories page
                if col2.button("Read More", key=f"read_more_{index}"):
                    go_to_page(f"Stories_{index}")
                    # Display content for each row
                st.divider()
            else:
                with st.container():
                    col1, col2 = st.columns([2, 1])

                        # Display the image if the path is not empty
                if pd.notna(row['Image Path']):
                    col2.image(row['Image Path'], width=400)  # Adjust the width as needed
             
                        # Display Header, Sub Header, and Text values
                if pd.notna(row['Header']):
                    col1.title(row['Header'])
                if pd.notna(row['Sub Header']):
                    col1.subheader(row['Sub Header'])
                if pd.notna(row['Text']):
                    col1.write(row['Text'])

                        # Add a "Read More" button to navigate to the stories page
                if col1.button("Read More", key=f"read_more_{index}"):
                    go_to_page(f"Stories_{index}")
                st.divider()
            
    for index1, row1 in data1.iterrows():
        if st.session_state.current_page == f"Stories_{index1}":
            st.markdown(
                """
                <h1 style='text-align: center; font-size: 60px; color: black;'>The Axtria Times</h1>
                """, 
                unsafe_allow_html=True
            )
            html_code = f"""
                <style>
                .img-container {{
                    text-align: center;
                }}
                .img-container img {{
                    width: 300px;
                    height:300px !important;
                }}
                </style>
                <div class="img-container">
                    <img src="data:image/png;base64,{st.image(row1['Image Path'])}" alt="High-Quality Image" height:"300px">
                </div>
            """

# Render the HTML in Streamlit
            #st.markdown(html_code, unsafe_allow_html=True)
           # if pd.notna(row1['Image Path']):
          #      st.image(row1['Image Path'], width=600)
        
            if pd.notna(row1['Header']):
                st.title(row1['Header'])
                
            if pd.notna(row1['Sub Header']):
                st.subheader(row1['Sub Header'])

            if pd.notna(row1['Text']):
                st.write(row1['Text'])

            if st.button("Back to Home"):
                go_to_page("Home")

except FileNotFoundError:
    st.error("File not found. Please check the file path.")
except Exception as e:
    st.error(f"An error occurred: {e}")