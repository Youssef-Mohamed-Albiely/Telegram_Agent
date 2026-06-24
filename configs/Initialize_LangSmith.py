import os 

def get_langsmith():
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY") 
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_PROJECT"] = "my_project"
    os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")