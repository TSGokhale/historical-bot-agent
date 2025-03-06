from flask import Flask, request, jsonify
from agent import chatbot, ChatState

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    state = ChatState()
    response = chatbot.invoke({"state": state, "user_input": user_input})

    return jsonify({"response": response[1]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
