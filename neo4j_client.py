from neo4j import GraphDatabase
from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def _record_to_dict(record):
    out = {}
    for key in record.keys():
        value = record[key]
        # if it's a Neo4j Node, convert to dict of properties
        if hasattr(value, "items"):  # Node, Relationship behave like dict-ish
            out[key] = dict(value)
        else:
            out[key] = value
    return out

def run_cypher(query: str, params: dict | None = None) -> list[dict]:
    with driver.session() as session:
        result = session.run(query, params or {})
        return [_record_to_dict(r) for r in result]
