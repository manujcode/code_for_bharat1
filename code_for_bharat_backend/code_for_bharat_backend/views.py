from django.http import HttpResponse, request, response,JsonResponse
from django.shortcuts import render
import json
import os
from pathlib import Path
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
# Update imports to use latest versions
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import OllamaLLM  # Updated import for Ollama
from langchain_qdrant import QdrantVectorStore  # Updated import for Qdrant
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate


def chat_with_bot(vector_store,request):
    # Define the LLM with a system prompt
    llm = OllamaLLM(
        model="mistral",
        system="""
        You are an Ayurvedic knowledge assistant. Your purpose is to provide accurate information about Ayurvedic from the context.
        
        When answering questions:
        1. you should answer questions based on the context provided in the context
        2. you should answer in friendly and concise language
        3. Base your responses on the Ayurvedic verses provided in the context
        4. Explain concepts clearly and in simple language
        5. If a question is outside the scope of Ayurveda or the provided verses, politely indicate this
        6. When quoting verses, clearly indicate the verse number
        7. Provide practical applications of Ayurvedic wisdom when appropriate
        8. if question is not related to ayurveda then you should reply with "I'm sorry, I'm not able to answer this question."
        9. you should answre to the point not increase the words,reply minimum words as possible as.
        10.you shoud not use verse number in reply.
        Remember that you are helping users understand ancient Ayurvedic knowledge in a modern context.
        """
    )

    # Create the retrieval chain using the updated API
    # Define the prompt template
    system_prompt = """
    You are an Ayurvedic knowledge assistant. Your purpose is to provide accurate information about Ayurvedic from the context.
    
    When answering questions:
    1. you should answer questions based on the context provided in the context
    2. you should answer in friendly and concise language
    3. Base your responses on the Ayurvedic verses provided in the context
    4. Explain concepts clearly and in simple language
    5. If a question is outside the scope of Ayurveda or the provided verses, politely indicate this
    6. When quoting verses, clearly indicate the verse number
    7. Provide practical applications of Ayurvedic wisdom when appropriate
    8. if question is not related to ayurveda then you should reply with "I'm sorry, I'm not able to answer this question."
    9.you must provide small ans and to the point as possible.
    10.if possible you sould ans in bullet point.
    11.you must use indian (Hindi + English) language to reply like a normal person or a doctor.
    
    Context: {context}
    """
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])
    
    # Create the document chain
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    
    # Create the retrieval chain
    qa_chain = create_retrieval_chain(
        vector_store.as_retriever(search_kwargs={"k": 4}),
        question_answer_chain
    )

    print("\n📚 Ayurveda Verse Chatbot Ready! Type 'exit' to quit.")
    
    query = json.loads(request.body) 
    query = query.get("query",'')
    print("-->",query)
    # query = "what is ayurveda?"
    # if query.lower() in ['exit', 'quit']:
    #     break
        # Use invoke method with the new chain structure
    res = qa_chain.invoke({"input": query})
        # Extract the answer from the response
    answer = res.get("answer", "I'm sorry, I couldn't find an answer.")
    return JsonResponse({"answer":answer})


# if _name_ == "_main_":
#     collection_name = "ayurveda_verses"
#     qdrant = QdrantClient(host="localhost", port=6333)
#     collections = [col.name for col in qdrant.get_collections().collections]
        
#     if collection_name not in collections:
#         print("No collections available. Please create a collection first.")
#         exit(1)
#         # Use regular embeddings for querying (no need for logging here)
#     embeddings = OllamaEmbeddings(model="mistral")    
#     vector_store = QdrantVectorStore(
#                 client=qdrant,
#                 collection_name=collection_name,
#                 embedding=embeddings
#             )   
#     print("[1] Launching the chatbot...")
#     chat_with_bot(vector_store)
def chat(request):
    collection_name = "ayurveda_verses"
    qdrant = QdrantClient(host="localhost", port=6333)
    collections = [col.name for col in qdrant.get_collections().collections]
        
    if collection_name not in collections:
        return HttpResponse("No collections available. Please create a collection first.")
        # exit(1)
        # Use regular embeddings for querying (no need for logging here)
    embeddings = OllamaEmbeddings(model="mistral")    
    vector_store = QdrantVectorStore(
                client=qdrant,
                collection_name=collection_name,
                embedding=embeddings
            )   
    print("[1] Launching the chatbot...")
    return chat_with_bot(vector_store,request)