from flask import Flask, request, jsonify
import os
import google.generativeai as genai

app = Flask(__name__)

# API KEY
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

@app.route("/")
def home():
    return """
    <h2>AI Recap Tool</h2>
    <form action="/generate" method="post">
        <textarea name="script" rows="8" cols="40"
        placeholder="ဒီနေရာမှာ script ထည့်ပါ..."></textarea><br><br>
        <button type="submit">Generate SSML</button>
    </form>
    """

@app.route("/generate", methods=["POST"])
def generate():
    script = request.form.get("script")

    if not script:
        return "No script provided"

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Convert this script into SSML format for natural Myanmar voice narration:

    {script}
    """

    response = model.generate_content(prompt)

    return f"<h3>SSML Result:</h3><pre>{response.text}</pre>"

if __name__ == "__main__":
    app.run()
