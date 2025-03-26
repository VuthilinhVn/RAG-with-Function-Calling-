# rag/data_processing.py
from dotenv import load_dotenv
import os
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
load_dotenv()
# Tạo LineTextSplitter tùy chỉnh để tách theo dòng
class LineTextSplitter:
    def split_text(self, text):
        return text.strip().split('\n')

# Khởi tạo splitter
text_splitter = LineTextSplitter()

# Sử dụng model embedding 3 của OpenAI
embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

# Định nghĩa hàm xử lý cho từng file
def process_text_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    documents = text_splitter.split_text(text)
    db = FAISS.from_texts(documents, embedding_model)
    db.save_local(output_path)
    print(f"✅ Đã xử lý và lưu Vector DB: {output_path}")

# Hàm chính để xử lý 3 file dữ liệu
def ingest_all():
    os.makedirs("db", exist_ok=True)

    process_text_file("data/booking_info.txt", "db/booking_index")
    process_text_file("data/products.txt", "db/products_index")
    process_text_file("data/reviews.txt", "db/reviews_index")

if __name__ == "__main__":
    ingest_all()
