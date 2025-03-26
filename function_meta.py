# rag/function_meta.py

functions_metadata = [
    {
        "name": "about_booking",
        "description": "查询特定日期和时间的场地预订信息，例如：2025/3/24.",
        "parameters": {
            "type": "object",
            "properties": {
                "info": {
                    "type": "string",
                    "description": "包含日期、时间、场地类型和位置的信息。例如：“'东华大学','7人制足球场', '2025/3/24', '19:00'"
                }
            },
            "required": ["info"]
        }
    },
    {
        "name": "about_products",
        "description": "查询BMB产品信息如名字、类型等等.",
        "parameters": {
            "type": "object",
            "properties": {
                "info": {
                    "type": "string",
                    "description": "查询内容, 比如: '俱乐部活动与成员管理'"
                }
            },
            "required": ["info"]
        }
    },
    {
        "name": "reviews_search",
        "description": "查询和总结用户对某种产品的评价.",
        "parameters": {
            "type": "object",
            "properties": {
                "info": {
                    "type": "string",
                    "description": "产品明细或产品描述, 比如: '预定系统的评价'"
                }
            },
            "required": ["info"]
        }
    }
]
