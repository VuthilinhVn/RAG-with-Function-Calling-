# rag/function_call_utils.py
import json

def remove_extra_quotes(function_call_string):
    start = function_call_string.find('{')
    end = function_call_string.rfind('}')
    if start != -1 and end != -1:
        json_string = function_call_string[start:end+1]
        try:
            json.loads(json_string)
            return json_string
        except json.JSONDecodeError:
            # xử lý các lỗi phổ biến
            json_string = json_string.replace("'", "\"").replace("\\", "")
            try:
                json.loads(json_string)
                return json_string
            except:
                return None
    return None

def remove_simulated_conversation(text):
    # loại bỏ phần mô phỏng "user:" trong response GPT
    index = text.find("user:")
    if index != -1:
        return text[index+6:]
    return text
