# 🌿 AyurSamvad: Your Personalized AI-Powered Ayurveda Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

AyurSamvad is an intelligent, conversational AI assistant designed to make the ancient wisdom of Ayurveda accessible and personalized for everyone. It leverages a powerful Retrieval-Augmented Generation (RAG) pipeline to provide accurate, context-aware answers to your health queries based on a vast knowledge base of Ayurvedic texts.

## 🎯 Problem Statement

Ayurvedic knowledge, while profound, is often locked away in complex texts, making it difficult for the average person to find reliable, personalized health advice. AyurSamvad bridges this gap by providing an intuitive chat interface that connects users with a sophisticated AI, delivering tailored Ayurvedic insights instantly.

## ✨ Features

- **Personalized Ayurvedic Chat**: Engage in natural conversations to get tailored health advice.
- **Powered by RAG**: Utilizes a Retrieval-Augmented Generation model for accurate and contextually relevant answers.
- **Modern & Intuitive UI**: A clean, responsive, and user-friendly interface built with React.
- **Real-time Interaction**: Get instant responses from the AI assistant.

## 📸 Screenshots

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)

`![Chat Interface](<path_to_screenshot.png>)`
*The main chat interface of AyurSamvad.*

## 🛠️ Technology Stack

This project uses a modern tech stack for both the frontend and backend.

| Component | Technology |
| :--- | :--- |
| **Frontend** | `React.js`, `React Hooks`, `Fetch API`, `CSS3` |
| **Backend** | `Python`, `Django` |
| **AI/ML** | `Retrieval-Augmented Generation (RAG)`, `LLMs`, `Vector Stores` |

## 🏗️ Architecture

The application follows a client-server architecture. The RAG pipeline is the core of the backend, enabling intelligent responses.

```
+----------------+      +------------------------+      +--------------------+
|                |      |                        |      |                    |
| User Interface |----->|   Django Backend API   |----->|    RAG Pipeline    |
| (React App)    |      |   (localhost:8000)     |      | (LangChain/Custom) |
|                |      |                        |      |                    |
+----------------+      +------------------------+      +----------+---------+
                                                                   |
                                                                   |
                                                     +-------------v-------------+
                                                     |                           |
                                                     | Large Language Model (LLM)  |
                                                     | & Vector Knowledge Base   |
                                                     |                           |
                                                     +---------------------------+
```

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

- Git
- Node.js & npm
- Python & pip

### Installation & Setup

**1. Clone the Repository**
```bash
git clone https://github.com/manujcode/code_for_bharat1.git
cd code_for_bharat1
```

**2. Backend Setup**
```bash
# Navigate to the backend directory
cd code_for_bharat_backend

# (Recommended) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install backend dependencies
pip install -r requirements.txt

# Run the Django development server
python manage.py runserver
```
The backend will be running at `http://127.0.0.1:8000`.

**3. Frontend Setup**
```bash
# Open a new terminal and navigate to the frontend directory
cd frontend-ayurveda-rag

# Install frontend dependencies
npm install

# Start the React development server
npm start
```
The frontend will be available at `http://localhost:3000`.

## 🤝 Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
