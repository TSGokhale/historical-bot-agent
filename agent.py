from langgraph.graph import StateGraph, END
from wikipedia_handler import search_monument_info
from email_verification import generate_otp, verify_otp

class ChatState:
    def __init__(self):
        self.email = None
        self.otp_requested = False
        self.verified = False

def initial_node(state, user_input):
    if "email" in user_input.lower():
        return "ask_email"
    else:
        response = search_monument_info(user_input)
        return "respond", response

def ask_email(state, user_input):
    state.email = user_input
    otp = generate_otp(state.email)
    state.otp_requested = True
    return "ask_otp", f"OTP sent to {state.email}, please provide the code."

def ask_otp(state, user_input):
    if verify_otp(state.email, user_input):
        state.verified = True
        return "verified", "Thanks, your email is verified. I'll send you more details soon."
    else:
        return "ask_otp", "Invalid OTP, please try again."

graph = StateGraph(ChatState)

graph.add_node("initial", initial_node)
graph.add_node("ask_email", ask_email)
graph.add_node("ask_otp", ask_otp)
graph.add_node("respond", lambda state, response: (END, response))
graph.add_node("verified", lambda state, response: (END, response))

graph.add_edge("initial", "respond")
graph.add_edge("initial", "ask_email")
graph.add_edge("ask_email", "ask_otp")
graph.add_edge("ask_otp", "ask_otp")
graph.add_edge("ask_otp", "verified")

chatbot = graph.compile()
