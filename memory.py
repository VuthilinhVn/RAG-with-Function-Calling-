# rag/memory_manual.py

def init_memory():
    """
    Khởi tạo bộ nhớ hội thoại dạng danh sách.
    """
    return [
        {
            "role": "system",
            "content": (
                "Bạn là một trợ lý hữu ích của một BMB, "
                "có quyền truy cập vào các chức năng như tra cứu sản phẩm, kiểm tra đơn đặt sân, và tổng hợp đánh giá khách hàng. "
                "Sử dụng function calling nếu cần để lấy dữ liệu chính xác."
            )
        }
    ]
