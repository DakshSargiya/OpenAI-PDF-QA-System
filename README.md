# Legal Contract Question-Answering System

## Overview
This tool helps users ask natural language questions about legal documents. It reads a PDF, processes the content, and uses an LLM to answer questions, providing citations from the document.

## Prerequisites
Python 3.10 or higher\
nltk\
PyPDF2\
Langchain\
openai

## Installation
1. Clone this repository to your local machine.
2. Install dependencies:
   `pip install openai PyPDF2 langchain nltk`

3. Upload one or more PDF files using the file uploader.

4. Ask a question about the content of the PDF files in the text input field.
5. The application will use the Langchain and Open AI to find the answer in the context of the PDF files and display it.

## Code Structure
* `project.py`: Main file.
* `_load_pdf`: A function to extract text from the uploaded PDF files.
* `_initialize_qa_chain`: A function to split the extracted text into smaller chunks, to create a conversational chain for question answering.
* `find_citations`: A function to find the context of the given answer
* `answer_question`: A function to find the answer to the given question using OpenAI
