# app.py

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from helper_function import about_booking, about_products, reviews_search
from function_call_utils import remove_extra_quotes, remove_simulated_conversation
from function_meta import functions_metadata
from memory import init_memory

# Load API key từ .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

app = FastAPI()

# Cho phép frontend truy cập từ localhost:3000 (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # hoặc ["http://localhost:3000"] nếu muốn cụ thể hơn
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schema đầu vào từ React
class ChatRequest(BaseModel):
    messages: list

@app.post("/chat")
async def chat(request: ChatRequest):
    messages = request.messages

    try:
        # Gửi request tới GPT
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            functions=functions_metadata,
            temperature=0
        )

        response_msg = response.choices[0].message

        # Nếu GPT muốn gọi hàm
        if response_msg.function_call:
            function_name = response_msg.function_call.name
            raw_args = remove_extra_quotes(response_msg.function_call.arguments)

            try:
                args = json.loads(raw_args)
            except:
                return {"reply": "❌ 无法解析参数。"}

            # Thực thi hàm tương ứng
            if function_name == "about_booking":
                result = about_booking(**args)
            elif function_name == "about_products":
                result = about_products(**args)
            elif function_name == "reviews_search":
                result = reviews_search(**args)
            else:
                result = f"❌ 未知函数：{function_name}"

            # Gửi lại function result để GPT trả lời đầy đủ
            messages.append({
                "role": "function",
                "name": function_name,
                "content": result
            })

            followup = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=0
            )

            final_reply = followup.choices[0].message.content
        else:
            final_reply = response_msg.content

        return {"reply": final_reply}

    except Exception as e:
        return {"reply": f"❌ Lỗi服务器: {str(e)}"}
