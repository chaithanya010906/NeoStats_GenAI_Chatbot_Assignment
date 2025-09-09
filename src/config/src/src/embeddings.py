# Placeholder for embeddings (future extension)
def get_embeddings(text: str):
    """Dummy embedding function"""
    return [ord(c) for c in text[:50]]  # simple vector of ASCII values
