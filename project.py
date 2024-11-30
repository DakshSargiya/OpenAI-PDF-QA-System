import sys
import openai
import nltk
from PyPDF2 import PdfReader
from langchain.llms import OpenAI
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA







class LegalQA:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.document_text = self._load_pdf()
        self.qa_chain = self._initialize_qa_chain()

    def _load_pdf(self):
        reader = PdfReader(self.pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    def _initialize_qa_chain(self):
        # Split the document into manageable chunks
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        texts = text_splitter.split_text(self.document_text)

        # Create embeddings for the text chunks
        embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

        # Use FAISS as the vector store
        vector_store = FAISS.from_texts(texts, embeddings)

        # Create a retriever
        retriever = vector_store.as_retriever()

        # Use the retriever with the LLM for question-answering
        llm = OpenAI(model="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=True)
        
        return qa_chain
    
    def find_citations(answer, document_text):
        
        answer_tokens = nltk.word_tokenize(answer)
        document_sentences = sent_tokenize(document_text)

        stop_words = set(stopwords.words('english'))
        answer_tokens = [token for token in answer_tokens if token not in stop_words]

        citations = []
        for i, sentence in enumerate(document_sentences):
            sentence_tokens = nltk.word_tokenize(sentence)
            
            similarity_score = jaccard_similarity(set(answer_tokens), set(sentence_tokens))
            
            citations.append((i+1, similarity_score))

        citations.sort(key=lambda x: x[1], reverse=True)

        return citations[:5]

    def answer_question(self, question):
        response = self.qa_chain.run(question)
        citations = self.find_citations(response, document_text)
        return response, citations

def main():
    if len(sys.argv) < 3:
        print("Usage: python question-answering.py /path/to/document 'question'")
        return

    pdf_path = sys.argv[1]
    question = sys.argv[2]

    qa_system = LegalQA(pdf_path)
    answer, context = qa_system.answer_question(question)
    print(f"Answer: {answer}")
    print(f"Context: {context}")

if __name__ == "__main__":
    main()
