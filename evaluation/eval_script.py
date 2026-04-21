import csv
import requests
import time
import json

EVAL_FILE = "evaluation/test_set.csv"
CHATBOT_URL = "http://0.0.0.0:8001/chat"
SEARCH_URL = "http://0.0.0.0:8001/search"

results = []

def evaluate():
    with open(EVAL_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            query = row['query']
            expected_file = row['expected_file']
            expected_answer = row['expected_answer']

            # Evaluate search endpoint
            search_data = {"query": query, "k": 5}
            start = time.perf_counter()
            search_resp = requests.post(SEARCH_URL, json=search_data)
            search_time = time.perf_counter() - start
            search_json = search_resp.json()

            # Extract key fields for search
            search_answer = search_json.get('message') or (search_json.get('matches')[0]['markdown'] if search_json.get('matches') else '')
            search_toxicity = search_json.get('toxicity_input', {}).get('label', '')

            # Evaluate chatbot endpoint
            chat_data = {"query": query, "k": 5}
            start = time.perf_counter()
            chat_resp = requests.post(CHATBOT_URL, json=chat_data)
            chat_time = time.perf_counter() - start
            chat_json = chat_resp.json()

            # Extract key fields for chat
            chat_answer = chat_json.get('answer', '')
            chat_toxicity = chat_json.get('toxicity_input', {}).get('label', '')

            results.append({
                "query": query,
                "expected_file": expected_file,
                "expected_answer": expected_answer,
                "search_time": search_time,
                "chat_time": chat_time,
                "search_response": json.dumps(search_json, ensure_ascii=False),
                "chat_response": json.dumps(chat_json, ensure_ascii=False),
                "search_answer": search_answer,
                "search_toxicity": search_toxicity,
                "chat_answer": chat_answer,
                "chat_toxicity": chat_toxicity
            })

    # Save results to CSV for later evaluation
    with open("evaluation/eval_results.csv", "w", newline='') as outfile:
        fieldnames = [
            "query", "expected_file", "expected_answer",
            "search_time", "chat_time",
            "search_answer", "search_toxicity",
            "chat_answer", "chat_toxicity",
            "search_response", "chat_response"
        ]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for r in results:
            writer.writerow({
                "query": r["query"],
                "expected_file": r["expected_file"],
                "expected_answer": r["expected_answer"],
                "search_time": round(r["search_time"], 3),
                "chat_time": round(r["chat_time"], 3),
                "search_answer": r["search_answer"],
                "search_toxicity": r["search_toxicity"],
                "chat_answer": r["chat_answer"],
                "chat_toxicity": r["chat_toxicity"],
                "search_response": r["search_response"],
                "chat_response": r["chat_response"]
            })
    print("Results saved to evaluation/eval_results.csv")

if __name__ == "__main__":
    evaluate()
