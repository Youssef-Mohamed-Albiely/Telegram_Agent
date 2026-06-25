from Agent.agent_ex import pipeline_with_history
from fastapi import FastAPI,Request
from Agent.initialize_llm import llm
import requests
import os

app = FastAPI()

access_token = os.getenv("ACCESS_TOKEN")

@app.post("/telegram-webhook")
async def receive_messages(request:Request):

    data = await request.json()
    try:
        if "message" in data and "text" in data["message"]:

            message = data["message"]
            chat_id = message["chat"]["id"]
            user_message = message["text"]
            user_id=message["from"]["id"]
            user_config = {"configurable":{"session_id":user_id , "k":20 , "llm":llm}}
            reply = pipeline_with_history.invoke({"input": user_message},config=user_config)
            
            send_message(chat_id,reply["output"])
    except Exception as e:
        return f"unexpected error{e}"
         

    return {"status":"ok"}
    
def send_message(chat_id,user_message):
    url = f"https://api.telegram.org/bot{access_token}/sendMessage"
    
    try:
        headers = {
            "Content-Type": "application/json"
        }
        
        payload = {
            "chat_id": chat_id,
            "text": user_message
        }
        
        response = requests.post(url, json=payload, headers=headers)

    except Exception as e:
        return f"unexpected error{e}"