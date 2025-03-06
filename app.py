from flask import Flask, request, jsonify, send_file
from agent import chatbot, ChatState

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('index.html')  # Serve the simple chat UI

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"error": "Please provide a 'message' field in JSON request."}), 400

    state = ChatState()
    next_node, response = chatbot.invoke(state, user_input)

    return jsonify({
        "response": response,
        "next_node": next_node
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
