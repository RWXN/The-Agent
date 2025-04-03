from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.tools.retriever import create_retriever_tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool

@tool
def real_time_search_tool(query: str) -> str:
    """For real time information search"""
    search = TavilySearchResults(max_results=1)
    return search

@tool
def summarize_website_tool(url: str) -> str:
    """For summarizing a website"""
    loader = WebBaseLoader(url)
    docs = loader.load()
    documents = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200).split_documents(docs)
    vector_store = FAISS.from_documents(documents, OpenAIEmbeddings())
    retriever = vector_store.as_retriever()
    retriever_tool = create_retriever_tool(
        retriever,
        name="retriever_tool",
        description="retrieve_information_from_a_website"
    )
    return retriever_tool




