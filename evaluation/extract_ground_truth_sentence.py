import pandas as pd
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv
import os
import re

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

def get_most_relevant_sentence(chunk_text, query):
    # Split chunk into sentences
    sentences = nltk.sent_tokenize(chunk_text)
    if not sentences:
        return chunk_text
    # Use TF-IDF to find the most similar sentence to the query
    vectorizer = TfidfVectorizer().fit(sentences + [query])
    sent_vecs = vectorizer.transform(sentences)
    query_vec = vectorizer.transform([query])
    sims = cosine_similarity(sent_vecs, query_vec).flatten()
    best_idx = np.argmax(sims)
    return sentences[best_idx]

# Paths
EVAL_CSV = 'evaluation/eval_results_chunks.csv'
EVAL_CSV_SENT = 'evaluation/eval_results_chunks_sentence.csv'

df = pd.read_csv(EVAL_CSV)

# Add a new column for sentence-level ground truth
sentences = []
for idx, row in df.iterrows():
    chunk_text = str(row.get('ground_truth', ''))
    query = str(row.get('query', ''))
    if chunk_text and chunk_text != '[NO CHUNK FOUND]':
        best_sentence = get_most_relevant_sentence(chunk_text, query)
    else:
        best_sentence = '[NO SENTENCE FOUND]'
    sentences.append(best_sentence)
df['ground_truth_sentence'] = sentences

df.to_csv(EVAL_CSV_SENT, index=False, quoting=csv.QUOTE_ALL)
print('Created evaluation/eval_results_chunks_sentence.csv with sentence-level ground truth.')
