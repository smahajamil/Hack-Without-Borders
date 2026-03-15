from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_llm(question, context):

    prompt = f"""
Answer the question using ONLY the provided context.

Context:
{context}

Question:
{question}

If the answer is not in the context, say information is unavailable or contains harmful biases. 
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text