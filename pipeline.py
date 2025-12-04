# pipeline.py

from llm_client import generate_cypher, explain_answer
from neo4j_client import run_cypher

def answer_question(question: str) -> dict:
    cypher = generate_cypher(question)
    rows = run_cypher(cypher)
    explanation = explain_answer(question, cypher, rows)

    return {
        "question": question,
        "cypher": cypher,
        "rows": rows,
        "answer": explanation,
    }
