from langgraph.graph import StateGraph, END, START
from wikipedia_handler import search_monument_info
from email_verification import generate_otp, verify_otp

class ChatState:
    def __init__(self):
        self.email = None
        self.otp_requested = False
        self.verified = False
        self.user_input = None  # New: store user input in the state


# Initial node — process user input and decide next step
def initial_node(state):
    user_input = state.user_input.lower()

    if "email" in user_input:
        return "ask_email"
    else:
        response = search_monument_info(user_input)
        return "respond", response


# Ask for email and send OTP
def ask_email(state):
    state.email = state.user_input
    otp = generate_otp(state.email)
    state.otp_requested = True
    return "ask_otp", f"OTP sent to {state.email}, please provide the code."


# Ask for OTP and verify it
def ask_otp(state):
    if verify_otp(state.email, state.user_input):
        state.verified = True
        return "verified", "Thanks, your email is verified. I'll send you more details soon."
    else:
        return "ask_otp", "Invalid OTP, please try again."


# Respond and end the conversation
def respond(state, response):
    return END, response


# Verified state — just acknowledges verification
def verified(state, response):
    return END, response


# Set up the graph
graph = StateGraph(ChatState)

# Nodes
graph.add_node("initial", initial_node)
graph.add_node("ask_email", ask_email)
graph.add_node("ask_otp", ask_otp)
graph.add_node("respond", respond)
graph.add_node("verified", verified)

# Edges
graph.add_edge("initial", "respond")
graph.add_edge("initial", "ask_email")
graph.add_edge("ask_email", "ask_otp")
graph.add_edge("ask_otp", "ask_otp")
graph.add_edge("ask_otp", "verified")

# Entry point
graph.add_edge(START, "initial")

# Compile the chatbot
chatbot = graph.compile()
