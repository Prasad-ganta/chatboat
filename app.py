from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY")) 
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"]

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": user_message}
            ]
        )

        reply = completion.choices[0].message.content

    except Exception as e:
        print("ERROR:", e)
        reply = "AI service error"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)