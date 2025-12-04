# llm_client.py

from openai import OpenAI
from config import OPENAI_API_KEY, SCHEMA_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_cypher(question: str) -> str:
    messages = [
        {"role": "system", "content": SCHEMA_PROMPT},
        {"role": "user", "content": question},
    ]
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0,
    )
    return resp.choices[0].message.content.strip()

def explain_answer(question: str, cypher: str, rows: list[dict]) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You explain Neo4j query results to factory engineers. "
                "Answer in 3–5 clear sentences, no markdown, no bullet points, "
                "no numbered lists, no headings. Just plain text."
            ),
        },
        {
            "role": "user",
            "content": (
                f"User question:\n{question}\n\n"
                f"Cypher query:\n{cypher}\n\n"
                f"Result rows (JSON):\n{rows}\n\n"
                "Explain what this result means in simple terms."
            ),
        },
    ]
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.2,
    )
    return resp.choices[0].message.content.strip()

