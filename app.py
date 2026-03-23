import os
from flask import Flask, request, jsonify
from groq_api import GroqClient  

app = Flask(__name__)
api_key = os.getenv("GROQ_API_KEY")
client = GroqClient(api_key=api_key)
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
