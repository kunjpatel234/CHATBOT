from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import google.generativeai as genai
import openai
import os

load_dotenv()

app = Flask(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MONGO_URI = os.getenv("MONGO_URI")

try:
    client = MongoClient(MONGO_URI)
    db = client["ai_agent"]
    collection = db["messages"]
    print("MongoDB connected.")
except Exception as e:
    print("MongoDB error:", e)
    exit()

genai.configure(api_key=GEMINI_API_KEY)
openai.api_key = OPENAI_API_KEY

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("user_input", "")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    ai_response = None

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(user_input)
        ai_response = response.text.strip()
        print("Gemini success.")
    except Exception as e:
        print("Gemini failed:", e)

    if not ai_response:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            ai_response = response.choices[0].message["content"].strip()
            print("OpenAI fallback success.")
        except Exception as e:
            print("OpenAI failed:", e)

    if not ai_response:
        ai_response = (
    "Due to limitations in our current AI access (such as exceeded quotas or no premium subscription "
    "on OpenAI or Gemini), the system is unable to generate a real-time response at the moment. "
    "Here’s a sample message instead: 'Thank you for your query. We'll get back to you shortly.'"
)


    collection.insert_one({
        "user_input": user_input,
        "ai_response": ai_response
    })

    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True)
