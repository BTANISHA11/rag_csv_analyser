import streamlit as st
import pandas as pd

# Initialize session state for uploaded files
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = {}

# Function to upload a CSV file
def upload_file(uploaded_file):
    if uploaded_file is not None:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(uploaded_file)
        file_id = uploaded_file.name
        st.session_state.uploaded_files[file_id] = df
        st.success(f"File '{file_id}' uploaded successfully!")
        return file_id
    return None

# Function to query the DataFrame
def query_data(file_id, query):
    if file_id in st.session_state.uploaded_files:
        df = st.session_state.uploaded_files[file_id]
        try:
            result = df.query(query)
            return result
        except Exception as e:
            st.error(f"Query error: {e}")
    else:
        st.error("File ID not found.")

# Function to delete a file
def delete_file(file_id):
    if file_id in st.session_state.uploaded_files:
        del st.session_state.uploaded_files[file_id]
        st.success(f"File '{file_id}' deleted successfully!")
    else:
        st.error("File ID not found.")

# Streamlit UI
st.title("RAG CSV Analyser")

# File Upload
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if st.button("Upload"):
    upload_file(uploaded_file)

# List Uploaded Files
st.subheader("Uploaded Files")
if st.session_state.uploaded_files:
    for file_id in st.session_state.uploaded_files.keys():
        st.write(file_id)
else:
    st.write("No files uploaded.")

# Query Data
st.subheader("Query the Data")
if st.session_state.uploaded_files:
    file_id = st.selectbox("Select File ID", list(st.session_state.uploaded_files.keys()))
    
    # Show a preview of the selected file
    st.write("Data Preview:")
    st.dataframe(st.session_state.uploaded_files[file_id].head())  # Show the first few rows of the selected file
    
    query = st.text_input("Enter your query (e.g., column_name == 'value')")
    if st.button("Run Query"):
        if query:
            result = query_data(file_id, query)
            if result is not None:
                st.write("Query Result:")
                st.dataframe(result)
        else:
            st.error("Please enter a query.")
else:
    st.write("Please upload a file to query.")

# Delete File
st.subheader("Delete a File")
if st.session_state.uploaded_files:
    delete_file_id = st.selectbox("Select File ID to Delete", list(st.session_state.uploaded_files.keys()))
    if st.button("Delete File"):
        delete_file(delete_file_id)
else:
    st.write("No files to delete.")

# Option to download the modified DataFrame
if st.session_state.uploaded_files:
    download_file_id = st.selectbox("Select File ID to Download", list(st.session_state.uploaded_files.keys()))
    if st.button("Download Modified Data"):
        modified_file = f"{download_file_id}_modified.csv"
        st.session_state.uploaded_files[download_file_id].to_csv(modified_file, index=False)
        st.success("Modified data saved!")
        st.download_button("Download CSV", modified_file)