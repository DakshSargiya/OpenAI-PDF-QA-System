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

3. Export your OpenAI API key on your terminal
    ```bash
    export OPENAI_API_KEY='OPENAI_API_KEY'
4. Usage: 
    ```bash 
    python3 question-answering.py /path/to/document "question    goes here"
    ```
5. It will use Langchain and Open AI to find the answer in the context of the PDF files and display it.

## Code Structure
* `project.py`: Main file.
* `_load_pdf`: A function to extract text from the uploaded PDF files.
* `_initialize_qa_chain`: A function to split the extracted text into smaller chunks, to create a conversational chain for question answering.
* `find_citations`: A function to find the context of the given answer
* `answer_question`: A function to find the answer to the given question using OpenAI

## Architecture Overview
* PDF Reading and Parsing:
   *Extract text from the PDF using PyPDF2.
* Text Splitting and Indexing:
   *Use langchain to split the text into manageable chunks for better LLM interaction.
* Question-Answering:
   *The extracted text is passed to the LLM along with the question.
   *Use langchain for better control over LLM prompting and context management.
* Citation of Source:
   *Retrieve the relevant chunk from the text that contains the answer and cite it in the response.
* Command-Line Interface:
   *Accepts a PDF path and a natural language question as inputs.
   *Returns the answer along with cited source material.

## Pitfalls
* Context Limitation: LLM has a context window limit.
* Legal Jargon Interpretation: Model may occasionally misinterpret highly specialized terms.
* Model Limitations: The LLM may not always provide accurate legal interpretations.
* Text Length Constraints: The API has limitations on input size which may truncate longer documents.
* Dependency on External API: Relying on an external service introduces latency and potential availability issues.

## Safeguards for Commercial Use
* Implement thorough testing with diverse legal documents to ensure reliability.
* Incorporate human oversight for critical legal tasks to verify AI-generated answers.
* Ensure compliance with data privacy regulations when handling sensitive legal documents.
* Fine-Tuning: Train on proprietary legal corpora.
* Audit Trails: Log responses and citations for accountability.
