
# Assigns a bias score to a text chunk using general rules.

# Bias score thresholds:
#   0 → safe
#   2 → flagged
#   3+  → blocked


import re

#Pattern groups that contribute to bias score
GENDER_ROLE_PATTERNS = [
    r"\bwomen (are|should|must|need to) (be |stay |remain )?(at home|nurturing|emotional|supportive|submissive)\b",
    r"\bmen (are|should|must) (be )?(strong|dominant|stoic|breadwinner|logical)\b",
    r"\b(naturally|inherently|biologically) (better|worse|suited|unfit)\b",
    r"\b(mothers|wives|females?) (belong|should stay|are best|are meant)\b",
]

STEREOTYPING_PATTERNS = [
    r"\ball (women|men|girls|boys|females?|males?) (are|act|think|feel|behave)\b",
    r"\b(women|men) (can't|cannot|don't|never) (lead|think|handle|manage)\b",
    r"\btypically (female|male|feminine|masculine)\b",
    r"\b(emotional|irrational|hysterical) (women|female|lady|ladies)\b",
]

DISCRIMINATORY_FRAMING_PATTERNS = [
    r"\b(only|just) a (woman|girl|female|lady)\b",
    r"\bfor a (woman|girl|female)\b",
    r"\b(despite being|even though she is) a woman\b",
    r"\b(working mothers?|female boss|lady doctor|female engineer)\b",
    r"\bwomen (don't|do not) belong\b",
]


def _count_pattern_matches(text, patterns):
    #Return the number of distinct patterns that match in text.
    text_lower = text.lower()
    count = 0
    for pattern in patterns:
        if re.search(pattern, text_lower):
            count += 1
    return count


def score_chunk(chunk_id, text):
    #Score a single text chunk for gender bias.
    score = 0
    score += _count_pattern_matches(text, GENDER_ROLE_PATTERNS) * 2
    score += _count_pattern_matches(text, STEREOTYPING_PATTERNS) * 2
    score += _count_pattern_matches(text, DISCRIMINATORY_FRAMING_PATTERNS) * 1

    if score <= 0:
        status = "safe"
    elif score <= 2:
        status = "flagged"
    else:
        status = "blocked"

    return {
        "chunk_id": chunk_id,
        "text": text,
        "bias_score": score,
        "status": status,
    }
