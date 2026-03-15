#Filters out biased chunks before passing context to the LLM.



def filter_chunks(chunks, allow_flagged: bool = True):

    approved = []
    blocked_ids = []

    for chunk in chunks:
        status = chunk["status"]

        if status == "blocked":
            blocked_ids.append(chunk["chunk_id"])
        elif status == "flagged" and not allow_flagged:
            blocked_ids.append(chunk["chunk_id"])
        else:
            approved.append(chunk)

    return approved, blocked_ids
