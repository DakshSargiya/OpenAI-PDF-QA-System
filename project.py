import sys
import openai
import nltk
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords



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
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
        texts = text_splitter.split_text(self.document_text)


        llm = OpenAI(model="gpt-4")
        qa_chain = RetrievalQA(llm=llm, retriever=texts)
        
        system_prompt = (
            "Use the given context to answer the question. "
            "If you don't know the answer, say you don't know. "
            "Use three sentence maximum and keep the answer concise. "
            "Context: {context}"
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        qa_chain = create_retrieval_chain(retriever, question_answer_chain)

        chain.invoke({"input": query})
        
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
