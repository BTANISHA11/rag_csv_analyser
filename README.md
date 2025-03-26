# RAG CSV Analyzer

## Overview
The RAG CSV Analyzer is a Streamlit application that allows users to upload, query, and manage CSV files. Users can perform operations such as viewing data previews, running queries, deleting files, and downloading modified data.

## Features
- **Upload CSV Files**: Users can upload CSV files, which are stored in memory.
- **View Uploaded Files**: A list of uploaded files is displayed for user reference.
- **Query Data**: Users can enter queries to filter the data in the uploaded CSV files.
- **Delete Files**: Users can delete uploaded files from memory.
- **Download Modified Data**: Users can download the modified DataFrame as a CSV file.

## Technologies Used
- [Streamlit](https://streamlit.io/): A framework for building web applications in Python.
- [Pandas](https://pandas.pydata.org/): A data manipulation and analysis library for Python.

## Setup Instructions

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd rag_csv_analyser
   ````

   Create a virtual environment (optional but recommended):
````
python -m venv venv
````
Activate the virtual environment:

For Windows:
````
venv\Scripts\activate
````
For macOS/Linux:

````
source venv/bin/activate
````
Install the required packages:
````
pip install -r requirements.txt
````
Running the Application
To run the Streamlit application, execute the following command:
````
streamlit run app.py
````
Open your web browser and navigate to http://localhost:8501 to access the application.

Usage Instructions
Upload CSV Files: Click on the "Upload CSV" button to upload your CSV files.
View Uploaded Files: A list of uploaded files will be displayed.
Query Data:
Select a file from the dropdown.
Enter your query in the text input box (e.g., column_name == 'value').
Click "Run Query" to see the filtered results.
Delete Files: Select a file from the dropdown and click "Delete File" to remove it from memory.
Download Modified Data: Select a file and click "Download Modified Data" to save the current DataFrame as a CSV file.
Example Queries
To filter rows where the City is "East Leonard":
````
City == 'East Leonard'
````
To filter rows where the Last Name is not "Baxter":
````
Last Name != 'Baxter'
````
To filter rows where the Company is "Steele Group" and the City is "Chavezborough":
````
Company == 'Steele Group' & City == 'Chavezborough'
`````

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Thanks to the Streamlit and Pandas communities for their excellent documentation and support.


### Summary of the README Sections

- **Overview**: Brief description of the application and its purpose.
- **Features**: List of functionalities provided by the application.
- **Technologies Used**: Technologies and libraries utilized in the project.
- **Setup Instructions**: Step-by-step guide to set up the project, including prerequisites and installation.
- **Running the Application**: Instructions on how to run the Streamlit app.
- **Usage Instructions**: Detailed usage instructions for the application.
- **Example Queries**: Examples of how to query the data.
- **License**: Licensing information.
- **Acknowledgments**: Credits to the communities or resources that helped in the development.
