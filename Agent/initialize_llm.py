from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

llm = ChatOpenAI(
api_key=os.getenv("GROQ_API_KEY"),
base_url="https://api.groq.com/openai/v1",
model="openai/gpt-oss-20b",
temperature=0.0
)
