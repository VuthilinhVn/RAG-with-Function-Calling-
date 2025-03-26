import { useState, useEffect, useRef } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const chatContainerRef = useRef(null);

  const isBotMessage = (msg) => msg.role === "assistant";

  const submitForm = async (e) => {
    e.preventDefault();
    if (!message.trim()) return;

    const userMessage = { role: "user", content: message };
    const updatedHistory = [...chatHistory, userMessage];
    setChatHistory([...updatedHistory, { role: "assistant", content: "⏳ 正在回复..." }]);
    setMessage("");

    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages: updatedHistory })
      });
      const data = await res.json();
      const reply = { role: "assistant", content: data.reply };
      setChatHistory([...updatedHistory, reply]);
    } catch {
      setChatHistory([...updatedHistory, { role: "assistant", content: "❌ Lỗi backend" }]);
    }
  };

  // Auto scroll xuống cuối khi có tin nhắn mới
  useEffect(() => {
    chatContainerRef.current?.scrollTo(0, chatContainerRef.current.scrollHeight);
  }, [chatHistory]);

  return (
    <div className="bg-gray-100 h-screen flex flex-col">
      <div className="container mx-auto p-4 max-w-2xl flex flex-col h-full">
        <h1 className="text-2xl font-bold mb-4">DHU-BMB Chatbot</h1>

        {/* Vùng chat */}
        <div
          className="flex-grow overflow-y-auto bg-white rounded shadow p-4 mb-4"
          ref={chatContainerRef}
        >
          {chatHistory.map((msg, i) => (
            <div key={i} className={`mb-2 ${isBotMessage(msg) ? "text-left" : "text-right"}`}>
              <p className="text-xs text-gray-500">{isBotMessage(msg) ? "Bot" : "User"}</p>
              <p className={`inline-block p-2 rounded-lg ${isBotMessage(msg) ? "bg-green-100" : "bg-blue-100"}`}>
                {msg.content}
              </p>
            </div>
          ))}
        </div>

        {/* Khung nhập đặt phía dưới */}
        <form className="flex" onSubmit={submitForm}>
          <input
            className="flex-grow p-2 rounded-l border"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="请输入..."
          />
          <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded-r">发送</button>
        </form>
      </div>
    </div>
  );
}

export default App;
