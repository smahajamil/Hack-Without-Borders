
#Split text into chunks and score each for bias.
#Returns a list of chunk dicts with id, text, bias_score, and status.
from scoring import score_chunk


def split_into_chunks(text):
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paragraphs


def scan_text(text):
    chunks = split_into_chunks(text)
    results = []

    for i, chunk_text in enumerate(chunks):
        chunk_id = f"chunk_{i + 1}"
        scored = score_chunk(chunk_id, chunk_text)
        results.append(scored)

    return results
