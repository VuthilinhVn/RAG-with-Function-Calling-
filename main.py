# rag/chatbot_main.py

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


# Load .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Khởi tạo OpenAI client
client = OpenAI(api_key=api_key)

# Thiết lập bộ nhớ hội thoại (system prompt)
# Khởi tạo bộ nhớ hội thoại
messages = init_memory()

# Vòng lặp chat
def run_chat():
    while True:
        user_input = input("🧑 You: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        messages.append({"role": "user", "content": user_input})

        try:
            # Gửi request tới GPT với function definitions
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                functions=functions_metadata,
                temperature=0
            )

            response_msg = response.choices[0].message

            # Nếu GPT yêu cầu gọi hàm
            if response_msg.function_call:
                function_name = response_msg.function_call.name
                function_args_raw = response_msg.function_call.arguments

                function_args_str = remove_extra_quotes(function_args_raw)

                try:
                    function_args = json.loads(function_args_str)
                except json.JSONDecodeError:
                    print("❌ Lỗi JSON trong arguments:", function_args_str)
                    continue

                # Gọi function phù hợp
                if function_name == "about_booking":
                    result = about_booking(**function_args)
                elif function_name == "about_products":
                    result = about_products(**function_args)
                elif function_name == "reviews_search":
                    result = reviews_search(**function_args)
                else:
                    result = f"Function {function_name} is not define."

                # Gửi kết quả lại cho GPT để tổng hợp trả lời
                messages.append({
                    "role": "function",
                    "name": function_name,
                    "content": result
                })

                final_response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=messages,
                    temperature=0
                )

                reply = final_response.choices[0].message.content
                print("🤖 Chatbot:", reply)
                messages.append({"role": "assistant", "content": reply})

            else:
                # Không cần gọi hàm, GPT trả lời trực tiếp
                reply = response_msg.content
                print("🤖 Chatbot:", reply)
                messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == "__main__":
    run_chat()
