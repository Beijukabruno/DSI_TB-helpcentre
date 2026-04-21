# answer_query.py
from semantic_search import search
from build_prompt import build_prompt
from call_gemma import call_gemma_model

def answer_query(user_query):
    results = search(user_query)
    prompt = build_prompt(user_query, results)
    response = call_gemma_model(prompt)
    return {
        "answer": response['response'],
        "sources": [meta for meta in results['metadatas'][0]]
    }

# Example usage
# result = answer_query("What are the side effects of TB treatment?")
# print(result["answer"])
# print(result["sources"])