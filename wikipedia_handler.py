import wikipedia
from filters import is_monument_related

def search_monument_info(query):
    if not is_monument_related(query):
        return "I'm only able to provide information about historical monuments. Please ask me about landmarks, historical buildings, or heritage sites."
    
    try:
        page = wikipedia.page(query)
        content = page.content
        return filter_monument_info(content)
    except Exception as e:
        return f"Sorry, I couldn't find information on that monument. Error: {e}"

def filter_monument_info(content):
    # Simple post-filter (can improve with regex or NLP later)
    sections = content.split("\n\n")
    filtered_sections = [sec for sec in sections if "history" in sec.lower() or "construction" in sec.lower() or "significance" in sec.lower()]
    return "\n\n".join(filtered_sections[:3])  # Return only top 3 relevant sections
