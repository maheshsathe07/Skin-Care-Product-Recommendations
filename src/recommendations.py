from langchain_community.embeddings import OllamaEmbeddings
import os
from pinecone import Pinecone
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
import google.generativeai as genai
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
embeddings=GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
# embeddings = OllamaEmbeddings(model="llama3")
index_name="recommend-products"

pinecone_api_key = os.getenv("PINECONE_API_KEY")
pc = Pinecone(api_key=pinecone_api_key)


def format_docs(docs):
    formatted_docs = []
    for doc in docs:
        metadata = doc.metadata
        formatted_doc = {
            "label": metadata.get('label', 'N/A'),
            "url": metadata.get('url', 'N/A'),
            "brand": metadata.get('brand', 'N/A'),
            "name": metadata.get('name', 'N/A'),
            "price": metadata.get('price', 'N/A'),
            "skin type": ', '.join(metadata.get('skin type', [])),
            "concern": metadata.get('concern', 'N/A'),
            "Reasoning": ""
        }
        formatted_docs.append(formatted_doc)
    return formatted_docs


class GeneralQuestionAnswering:
    def __init__(self):
        # Load environment variables
        load_dotenv()

        # Configure the Gemini model with the API key
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        # self.model = genai.model("gemini-pro")
        self.model = ChatGoogleGenerativeAI(model="gemini-pro")

    def ask_question(self, question, context):
        # Define the prompt template
        prompt_template = """
            Recommend product based on the user's query and the provided context only. 
            Only recommend product if they are in the context and relevant.  
            Provide three to five relevant products recommendations, ensuring from the context only. 
            If the context is empty or none of the products are relevant, dont give anything you can return empty json response.
            Do not recommend more than five products.
            Don't give answer on based of your knowledge, you are strictly to use context provided for recommending the products only.
            
            your response should be in json format only strictly.
            
            Use Context provided to give output of recommended products in the below mentioned format for every products, In the reasoning field in the output format, write your reason for recommending the product make it as you are explaining why its a must watch product:-
            
            OUTPUT FORMAT:
            [
                "label": "",
                "url": "",
                "brand":""
                "name": "",
                "price": "",
                "skin type": "",
                "concern": "",
                "Reasoning": ""
            ]
            
            Question: {question}
            Context: {context}
            """
        
        doc1  = format_docs(context)
        # print(doc1)
        prompt = prompt_template.format(question=question, context = doc1)
        # print(prompt)

        # Generate a response using the Gemini model
        response = self.model.invoke(prompt)
        # print(response)

        return response.content

