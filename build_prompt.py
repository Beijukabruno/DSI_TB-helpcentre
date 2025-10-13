# build_prompt.py
def build_prompt(user_query, results):
    prompt = (
        "You are a TB help centre assistant. Answer the following question using ONLY the provided information. "
        "Always cite the source for each fact.\n\n"
        f"Question: {user_query}\n\nRelevant Information:\n"
    )
    for i, (doc, meta) in enumerate(zip(results['documents'][0], results['metadatas'][0]), 1):
        prompt += f"{i}. {doc} (Source: {meta['source_file']}, Section: {meta['header']})\n"
    prompt += "\nYour answer:"
    return prompt

# Example usage
# prompt = build_prompt(user_query, results)