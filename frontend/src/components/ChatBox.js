import { useState } from "react";
import axios from "axios";

export default function ChatBox() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    const res = await axios.post("http://localhost:8000/ai/query", {
      query: input
    });

    setMessages([...messages, { user: input, bot: res.data.response }]);
    setInput("");
  };

  return (
    <div>
      {messages.map((m, i) => (
        <div key={i}>
          <p>User: {m.user}</p>
          <p>Bot: {m.bot}</p>
        </div>
      ))}
      <input value={input} onChange={e => setInput(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}