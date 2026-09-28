import os
from flask import Flask, jsonify, request, send_from_directory
from dotenv import load_dotenv
from google import genai

load_dotenv()
app = Flask(__name__, static_folder=".")

@app.get("/")
def index():
    return send_from_directory(".", "index.html")

@app.post("/api/chat")
def chat():
    try:
        data = request.get_json(silent=True) or {}
        messages = data.get("messages", [])
        api_key = os.getenv("GEMINI_API_KEY") or data.get("api_key")
        model = os.getenv("GEMINI_MODEL", "gemini-3.1-flash-lite")
        if not api_key or api_key == "YOUR_GEMINI_API_KEY":
            return jsonify(success=False, error="Gemini API key is not configured."), 400
        if not messages:
            return jsonify(success=False, error="No messages supplied."), 400
        client = genai.Client(api_key=api_key)
        contents = []
        for m in messages:
            role = "user" if m.get("role") == "user" else "model"
            contents.append({"role": role, "parts": [{"text": str(m.get("content", ""))}]})
        response = client.models.generate_content(model=model, contents=contents)
        text = getattr(response, "text", None)
        if not text:
            return jsonify(success=False, error="Gemini returned an empty response."), 502
        return jsonify(success=True, response=text)
    except Exception as exc:
        return jsonify(success=False, error=str(exc)), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
