from flask import Flask, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

# API KEY
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/")
def home():
    return "AI Recap Tool is Running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    script = data.get("script")

    if not script:
        return jsonify({"error": "No script provided"}), 400

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Convert this script into SSML format for natural Myanmar voice narration:

    {script}
    """

    response = model.generate_content(prompt)

    return jsonify({
        "ssml": response.text
    })

if __name__ == "__main__":
    app.run()
