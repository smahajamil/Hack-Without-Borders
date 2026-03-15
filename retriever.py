#Finds the most relevant chunks for a user question using simple keyword overlap scoring.


#Count how many question words appear in the chunk.
def _keyword_score(question, chunk_text):

    #Strip short stop words
    stop_words = {"the", "a", "an", "is", "are", "was", "were", "in", "on",
                  "at", "to", "of", "and", "or", "for", "with", "that", "this",
                  "it", "do", "how", "why", "what", "who", "which", "be"}

    question_words = set(question.lower().split()) - stop_words
    chunk_lower = chunk_text.lower()

    return sum(1 for word in question_words if word in chunk_lower)


def retrieve_relevant_chunks(question, chunks, top_n: int = 5):

    #Rank all chunks by keyword relevance to the question.
    #Returns the top_n most relevant chunks (regardless of bias status).

    scored = []
    for chunk in chunks:
        score = _keyword_score(question, chunk["text"])
        scored.append((score, chunk))

    #Sort by descending relevance
    scored.sort(key=lambda x: x[0], reverse=True)
    top = [chunk for score, chunk in scored if score > 0]

    # Fallback: if no keyword overlap found, return top_n by position
    if not top:
        top = [chunk for _, chunk in scored[:top_n]]

    return top[:top_n]
