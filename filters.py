# Simple keyword-based (can be expanded to use an ML classifier if needed)

HISTORICAL_KEYWORDS = [
    "monument", "historical", "heritage", "ancient", "landmark", 
    "palace", "castle", "temple", "church", "fort", "mosque", 
    "ruins", "tomb", "structure", "site", "pyramid", "mausoleum", "architecture"
]

def is_monument_related(query):
    query_lower = query.lower()
    return any(word in query_lower for word in HISTORICAL_KEYWORDS)
