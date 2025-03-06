from flask import Flask, request, jsonify
from agent import chatbot, ChatState

app = Flask(__name__)

# Root route to check if service is running
@app.route('/')
def home():
    return "Welcome to the chatbot service! Use /chat to talk to the bot."

# Chat route to interact with the chatbot
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Please provide a 'message' field in JSON request."}), 400

    # Initialize chatbot state
    state = ChatState()

    # Start conversation
    next_node, response = chatbot.invoke(state, user_input)

    return jsonify({
        "response": response,
        "next_node": next_node  # Optional - useful for debugging
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
