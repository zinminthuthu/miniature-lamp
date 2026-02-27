from flask import Flask, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return "AI Recap Tool is Running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    user_text = data.get("text")

    prompt = f"""
    Rewrite this script as a short engaging video recap.
    Also convert it into SSML format for voice generation.

    Script:
    {user_text}
    """

    response = model.generate_content(prompt)

    return jsonify({
        "result": response.text
    })

if __name__ == "__main__":
    app.run()
