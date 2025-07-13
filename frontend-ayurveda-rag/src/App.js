import React, { useState, useRef, useEffect } from 'react';
import { FaPaperPlane } from 'react-icons/fa';
import axios from 'axios';
import './App.css';

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async () => {
    if (input.trim() === '') return;

    // Add user message
    const newMessage = { text: input, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, newMessage]);
    setInput('');

    // Show typing indicator
    const tempMessageId = Date.now();
    setMessages(prev => [...prev, { 
      id: tempMessageId,
      text: '...', 
      sender: 'bot', 
      isTyping: true 
    }]);

    try {
      // Make POST request to the chat endpoint
      const response = await fetch('http://127.0.0.1:8000/chat/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: input })
      });

      if (!response.ok) {
        const error = await response.text().catch(() => 'No error details');
        throw new Error(`HTTP error! status: ${response.status}, message: ${error}`);
      }
       console.log("xx",response);
      // Parse the JSON response
      const responseData = await response.json();
      
      // Update the message with the response
      setMessages(prev => {
        const filtered = prev.filter(msg => msg.id !== tempMessageId);
        return [...filtered, { 
          id: tempMessageId,
          text: responseData.answer || 'No response from server',
          sender: 'bot'
        }];
      });
      
    } catch (error) {
      console.error('Error:', error);
      setMessages(prev => {
        const filtered = prev.filter(msg => msg.id !== tempMessageId);
        return [...filtered, { 
          id: tempMessageId,
          text: `Error: ${error.message}`,
          sender: 'bot',
          isError: true
        }];
      });
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSendMessage();
    }
  };

  return (
    <div className="App" style={{
      backgroundImage: `url(${process.env.PUBLIC_URL}/image.jpeg)`,
      backgroundSize: 'cover',
      backgroundPosition: 'center',
      backgroundRepeat: 'no-repeat',
      minHeight: '100vh',
      display: 'flex',
      flexDirection: 'column'
    }}>
      <header className="App-header">
        <h1>Ayurveda RAG Chat</h1>
      </header>
      <div className="chat-window" style={{
        backgroundColor: 'transparent',
        borderRadius: '10px',
        padding: '20px',
        margin: '20px',
        flexGrow: 1,
        overflowY: 'auto'
      }}>
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <div className="chat-input">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Type your message..."
        />
        <button onClick={handleSendMessage}>
          <FaPaperPlane />
          {/* Send */}
        </button>
      </div>
    </div>
  );
}

export default App;
