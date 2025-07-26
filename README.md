# AI Chat Assistant

This project is a lightweight AI-powered chatbot built using Flask, Google Gemini / OpenAI APIs, and MongoDB. It is designed to demonstrate API integration, database storage, and frontend-backend communication.

## Features

* Accepts user input via a simple frontend UI
* Responds using Gemini (primary) or OpenAI (fallback)
* Provides a sample message if both APIs fail (due to quota limits or missing access)
* Stores all conversations in MongoDB for review and logging

## Folder Structure

```
ai-agent-mvp/
  ├── backend/
  │   ├── main.py
  │   ├── .env
  │   ├── templates/
  │   │   └── index.html
  │   └── venv/
```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/ai-agent-mvp.git
cd ai-agent-mvp/backend
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install flask pymongo python-dotenv openai google-generativeai
```

### 4. Add Environment Variables

Create a `.env` file in the `backend/` folder:

```env
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
MONGO_URI=mongodb://localhost:27017
USE_GEMINI=True
```

## Running the Application

```bash
python main.py
```

Open a browser and go to:

```
http://127.0.0.1:5000
```

## Behavior When Quota Exceeds

If both Gemini and OpenAI APIs fail, the system will show a fallback message:

```
Due to limitations in our current AI access (such as exceeded quotas or no premium subscription on OpenAI or Gemini), the system is unable to generate a real-time response at the moment. Here’s a sample message instead: 'Thank you for your query. We'll get back to you shortly.'
```

## Notes

* Ensure MongoDB is running locally or provide a valid MongoDB Atlas connection string.
* Keep `.env` file private.
