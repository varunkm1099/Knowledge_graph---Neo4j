# main.py

from pipeline import answer_question

def main():
    question = input("Ask a question about failures: ")
    result = answer_question(question)

    print("\nGenerated Cypher:\n", result["cypher"])
    print("\nRaw rows:\n", result["rows"])
    print("\nAnswer:\n", result["answer"])

if __name__ == "__main__":
    main()
