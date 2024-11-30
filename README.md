# OpenAI-PDF-QA-System

Prerequisites
Python 3.10 or higher
Streamlit
PyPDF2
Langchain
Google Generative AI
Google Cloud SDK
Installation
Clone this repository to your local machine.
Create a virtual environment and activate it.
Install the required packages by running pip install -r requirements.txt
Create a .envfile in the root directory of the project and add your Google API key:
GOOGLE_API_KEY=<your_google_api_key>
Run the application by executing streamlit run app.py
Usage
Upload one or more PDF files using the file uploader.
Click the "submit & process" button to extract text from the PDF files.
Ask a question about the content of the PDF files in the text input field.
The application will use the Langchain and Google Generative AI to find the answer in the context of the PDF files and display it.
Code Structure
app.py: The main Streamlit application.
get_pdf_text: A function to extract text from the uploaded PDF files.
get_text_chunks: A function to split the extracted text into smaller chunks.
get_vector_store: A function to create a vector database for the text chunks.
get_conversional_chain: A function to create a conversational chain for question answering.
user_input: A function to handle user input and generate answers.
main: The main function that sets up the Streamlit application and runs the user input function.
