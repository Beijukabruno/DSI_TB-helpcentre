from transformers import pipeline

model_path = 'Intel/toxic-prompt-roberta'
pipe = pipeline('text-classification', model=model_path, tokenizer=model_path)

SAFE_RESPONSE = "Sorry, I can't assist with that."

def check_toxicity(text):
    result = pipe(text)[0]
    return result['label'], result['score']

def guard_input(text):
    label, score = check_toxicity(text)
    if label == 'TOXIC':
        return False, label, score, SAFE_RESPONSE
    return True, label, score, None

def guard_output(text):
    label, score = check_toxicity(text)
    if label == 'TOXIC':
        return False, label, score, SAFE_RESPONSE
    return True, label, score, None
