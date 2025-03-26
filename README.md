# RAG-with-Function-Calling-
Đây là dự án demo xây dựng 1 chatbot sử dụng hệ thống RAG tích hợp Function Calling hoàn chỉnh.

**Giới thiệu 介绍**

RAG_function_calling là một kho lưu trữ chứa mã để tạo ra các cuộc gọi hàm bằng mô hình Retrieval-Augmented Generation (RAG) tích hợp phương thức function calling. Mô hình này được sử dụng để tạo văn bản tự nhiên bằng cách lấy thông tin từ đoạn văn bản có sẵn.
RAG_function_calling 是一个用于实现函数调用的代码仓库，基于 RAG（Retrieval-Augmented Generation，检索增强生成）模型构建。该模型通过集成函数调用机制，能够从已有的文本片段中检索信息，并生成自然语言文本。
**Yêu cầu 要求**

Để sử dụng kho lưu trữ này, bạn cần phải có khóa API hợp lệ từ:
想要使用此代码仓库，您需要拥有来自以下服务的有效 API 密钥：
* **OpenAI:** https://platform.openai.com/docs/api-reference/introduction
* **Google AI:** https://cloud.google.com/ai-platform/docs/authentication/api-keys

**Lưu ý 注意**

Đừng bao giờ để api key của bạn trực tiếp trong code, hãy để vào file ".evn" nhé!
千万不要将您的 API 密钥直接写在代码中，应该将其保存在名为 .env 的环境变量文件中以确保安全！
```.evn
OPENAI_API_KEY = sk-...
```
```python
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
```

