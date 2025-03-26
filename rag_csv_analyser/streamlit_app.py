import streamlit as st
import requests

API_URL = "http://localhost:8000"  # Ensure this matches your FastAPI server URL

st.title("RAG CSV Analyser")

# File Upload
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file is not None:
    response = requests.post(f"{API_URL}/upload", files={"file": uploaded_file})
    
    # Check if the response is successful
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error(f"Error: {response.status_code}")
        st.write(response.text)  # Print the raw response text for debugging

# List Files
if st.button("List Files"):
    response = requests.get(f"{API_URL}/files")
    
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.error(f"Error: {response.status_code}")
        st.write(response.text)

# Query File
file_id = st.text_input("File ID")
query = st.text_input("Query")
if st.button("Query File"):
    if file_id and query:  # Ensure both fields are filled
        response = requests.post(f"{API_URL}/query", json={"file_id": file_id, "query": query})
        
        if response.status_code == 200:
            try:
                st.write(response.json())
            except ValueError:
                st.error("Response is not valid JSON.")
                st.write(response.text)  # Print the raw response text for debugging
        else:
            st.error(f"Error: {response.status_code}")
            st.write(response.text)  # Print the raw response text for debugging
    else:
        st.error("Please provide both File ID and Query.")

# Delete File
delete_file_id = st.text_input("File ID to delete")
if st.button("Delete File"):
    if delete_file_id:  # Ensure the field is filled
        response = requests.delete(f"{API_URL}/file/{delete_file_id}")
        
        if response.status_code == 200:
            st.write(response.json())
        else:
            st.error(f"Error: {response.status_code}")
            st.write(response.text)  # Print the raw response text for debugging
    else:
        st.error("Please provide a File ID to delete.")